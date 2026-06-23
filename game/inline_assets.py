#!/usr/bin/env python
"""Shrink + base64-inline the sprite art into index.html so the game is a single
self-contained file (double-click anywhere, no server). Idempotent."""
import os, io, base64, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "assets")
HTML = os.path.join(HERE, "index.html")

# js-key -> (filename, max dimension).  Featured art bigger; props smaller.
ASSETS = {
    "hero":     ("hero_idle.png", 380), "heroEmpty": ("hero_empty.png", 380),
    "heroRun": ("hero_run.png", 360),
    "heroCool": ("hero_cool.png", 360), "boombox": ("boombox.png", 300),
    "fishchips":("food_fishchips.png",200), "fries":("food_fries.png",200),
    "hush":     ("food_hushpuppies.png",200), "pie":("food_pie.png",200),
    "pudding":  ("food_pudding.png",200), "drink":("drink.png",200),
    "raw":      ("food_raw.png",200), "napkins":("napkins.png",160),
}

def data_uri(path, maxd):
    im = Image.open(path).convert("RGBA")
    if max(im.size) > maxd:
        s = maxd / max(im.size)
        im = im.resize((max(1,int(im.size[0]*s)), max(1,int(im.size[1]*s))), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    b = buf.getvalue()
    return "data:image/png;base64," + base64.b64encode(b).decode(), len(b)

parts, totbytes = [], 0
for key, (fn, maxd) in ASSETS.items():
    uri, n = data_uri(os.path.join(A, fn), maxd)
    totbytes += n
    parts.append(f'  "{key}":"{uri}"')
js = "<script>window.ASSET_DATA={\n" + ",\n".join(parts) + "\n};</script>"

with open(HTML, "r", encoding="utf-8") as f:
    html = f.read()
block = "<!--ASSET_DATA_START-->" + js + "<!--ASSET_DATA_END-->"
html = re.sub(r"<!--ASSET_DATA_START-->.*?<!--ASSET_DATA_END-->", lambda m: block, html, flags=re.S)
with open(HTML, "w", encoding="utf-8") as f:
    f.write(html)

print(f"inlined {len(ASSETS)} sprites, ~{totbytes/1024:.0f} KB raw PNG, html now {os.path.getsize(HTML)/1024:.0f} KB")
