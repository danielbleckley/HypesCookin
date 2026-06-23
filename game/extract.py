#!/usr/bin/env python
"""Auto-detect sprites on a white-background sheet, crop each, knock out the
white background to transparency, and save trimmed PNGs."""
import sys, os
import numpy as np
from PIL import Image
from scipy import ndimage

SRC = sys.argv[1]
OUTDIR = sys.argv[2]
PREFIX = sys.argv[3]
MIN_FRAC = float(sys.argv[4]) if len(sys.argv) > 4 else 0.004  # min area as frac of sheet

os.makedirs(OUTDIR, exist_ok=True)
img = Image.open(SRC).convert("RGBA")
# downscale big sheets for speed of detection, keep full for crop
W, H = img.size
arr = np.asarray(img)
rgb = arr[:, :, :3].astype(np.int16)

# "ink" = not near-white
white = (rgb[:, :, 0] > 238) & (rgb[:, :, 1] > 238) & (rgb[:, :, 2] > 238)
ink = ~white
# close small gaps so a sprite is one blob
ink = ndimage.binary_dilation(ink, iterations=6)
ink = ndimage.binary_fill_holes(ink)
labels, n = ndimage.label(ink)
print(f"{os.path.basename(SRC)}: {n} raw blobs, size {W}x{H}")

slices = ndimage.find_objects(labels)
sheet_area = W * H
boxes = []
for i, sl in enumerate(slices, start=1):
    if sl is None:
        continue
    ys, xs = sl
    h = ys.stop - ys.start
    w = xs.stop - xs.start
    area = w * h
    if area < sheet_area * MIN_FRAC:
        continue
    boxes.append((xs.start, ys.start, xs.stop, ys.stop, area))

# sort top-to-bottom, then left-to-right (row-major)
boxes.sort(key=lambda b: (round(b[1] / (H / 6)), b[0]))
print(f"  kept {len(boxes)} sprites")

PAD = 12
for idx, (x0, y0, x1, y1, area) in enumerate(boxes):
    x0 = max(0, x0 - PAD); y0 = max(0, y0 - PAD)
    x1 = min(W, x1 + PAD); y1 = min(H, y1 + PAD)
    crop = img.crop((x0, y0, x1, y1))
    c = np.asarray(crop).copy()
    cr = c[:, :, :3].astype(np.int16)
    # alpha: transparent where near-white
    nearwhite = (cr[:, :, 0] > 232) & (cr[:, :, 1] > 232) & (cr[:, :, 2] > 232)
    # only knock out white connected to the border (keeps white highlights inside art)
    keep = ~nearwhite
    keep = ndimage.binary_fill_holes(keep)  # fill interior whites back in
    alpha = (keep * 255).astype(np.uint8)
    # soften edge a touch
    alpha = ndimage.grey_erosion(alpha, size=(2, 2))
    c[:, :, 3] = alpha
    out = Image.fromarray(c, "RGBA")
    # trim fully-transparent margins
    bbox = out.getbbox()
    if bbox:
        out = out.crop(bbox)
    # cap max dimension to keep files small
    MAXD = 420
    if max(out.size) > MAXD:
        s = MAXD / max(out.size)
        out = out.resize((int(out.size[0]*s), int(out.size[1]*s)), Image.LANCZOS)
    name = f"{PREFIX}_{idx:02d}.png"
    out.save(os.path.join(OUTDIR, name))
    print(f"  {name}  {out.size[0]}x{out.size[1]}  (src area {area})")
