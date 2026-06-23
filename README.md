# HYPE'S COOKINN 🐟🎤

A mobile-web arcade game for the real-life Hype's Cookinn fish & chips pop-up —
soul food, hip hop, and a fish MC named **Hype**.

Run to the fridge for a fillet, fry it, and serve the line before they bail —
all while keeping the **boombox on hip hop**. The second it drifts to country,
the whole line starts walking out. 🤠➡️🚪

## ▶️ Play it
**🎮 Play now (any device): https://danielbleckley.github.io/HypesCookin/**

- **Live:** the link above runs the game in any browser — phone, tablet, or desktop.
- **Single file:** open [`HypesCookinn.html`](HypesCookinn.html) (or [`index.html`](index.html))
  in any browser. All art is inlined, so it works offline with nothing attached.
- **From source:** the same game lives at [`game/index.html`](game/index.html).
  To serve locally: `cd game && python3 -m http.server 8753`.

## 🎮 How to play
Tap a station and Hype runs there and does the job (no D-pad):
1. **Fridge** → grab a fillet (tap again to put it back — never get stuck).
2. **Fryer** → drop it in a vat (4s cook), tap again when READY to grab the plate.
3. **Tap a customer** → serve. Quick serves build a combo for more $.
4. **Boombox** → tap to scratch the music back to hip hop before the line bails.
5. **Messy tables** → wipe them to seat more dine-in customers (who tip).

Your wandering chef helper sometimes pitches in to fry. Hit **🎤 Meet the Cast**
on the title screen to see the crew.

## 🛠️ Project layout
```
HypesCookinn.html        self-contained build (art inlined) — the thing you share
game/
  index.html             source game (also self-contained)
  assets/                extracted sprite art (knocked out from the branding sheets)
  extract.py             auto-detects + trims sprites from the design sheets
  inline_assets.py       shrinks + base64-inlines the sprites into index.html
  README.md              dev notes + tuning knobs
```

### Rebuilding the inlined art
After changing anything in `game/assets/`, re-inline it:
```
cd game && python3 inline_assets.py   # needs Pillow
```
This regenerates the `ASSET_DATA` block in `index.html`. Then copy it up to the
root (`cp game/index.html HypesCookinn.html`) to refresh the shareable file.

> The original `.psd`/`.tif` design files and full-res AI renders are kept out of
> this repo (too large for GitHub). They live with the project owner.

🤖 Built with [Claude Code](https://claude.com/claude-code)
