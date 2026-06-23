# HYPE'S COOKINN 🐟🎤 — Fish, Chips & Hip Hop

A Tapper-style mobile-web game starring the Hype's Cookinn fish mascot. One self-contained
file (`index.html`) + sprite art knocked out from the real branding sheets.

## Run it
`index.html` is **fully self-contained** — all the art is inlined, so you can just
**double-click it** (or text/AirDrop the single file) and it works anywhere, no server.

For phone testing over Wi-Fi you can still serve it:
```
cd game && python3 -m http.server 8753
```
then open `http://<your-computer-ip>:8753` on your phone.

## How to play
Tap a station — Hype runs there and does the job automatically (no D-pad):
1. **Fridge** → grab a frozen fillet. Tap the fridge **again to put it back** if your hands are
   full or the fryer's jammed — you can never get stuck holding a fish.
2. **Fryer** → drop the fillet in an open vat (4s cook). Tap again when **READY** to grab the hot plate.
3. **Tap a waiting customer** → serve. Fast back-to-back serves build a **combo** (= more $).
   Hype stays wherever you last sent him — no auto-walking back to a home spot.
4. **Boombox** → the music meter drifts from HIP HOP toward COUNTRY. In the country zone the
   whole line loses patience fast and bails (lost heart). Tap the boombox to scratch it back to hip hop.
5. **Dirty tables** → diners leave a mess; tap to wipe. Clean tables let you seat more dine-in
   customers (who tip), so cleaning pays off.

Your **chef helper** just roams the floor on his own — sometimes he grabs a fillet and fries it
for you, sometimes he just wanders. Nice when he helps, but don't count on him.

5 hearts. A customer rage-quitting costs one. Score rolls into harder "days" (faster spawns + faster
music drift). Tap the 🔊 in the corner to mute.

## Tuning (top of the `<script>` in index.html)
| Constant | Does |
|---|---|
| `COOK_TIME` | seconds to fry a plate (4.0) |
| `BASE_PATIENCE` | how long a customer waits (17s) |
| `MUSIC_DRIFT_BASE` | how fast music slides to country |
| `COUNTRY_DRAIN` | patience-drain multiplier while country plays (2.8x) |
| `EAT_TIME` | how long diners sit before leaving a dirty table |
| `HERO_SPD` / `HELPER_SPD` | walk speeds |

## Assets
`assets/*.png` were auto-extracted from the branding sheets by `extract.py` (detects each sprite,
trims it, knocks the white background to transparency). The `assets/raw/` folder holds the full
extracted set (extra mascot poses, etc.) if you want to swap art in.

### Easy art swaps
- Main character: `hero_idle.png` (standing) / `hero_run.png` (carrying food).
- Music device: `boombox.png` (swap for a turntable render anytime).
- Menu items customers can order: edit `FOOD_KEYS` and the `IMG` map.

## Ideas to build next
- Per-customer order matching (must serve the exact item they want).
- Drinks/sides as a second prep station.
- A "hype meter": serving on-beat while hip hop plays gives bonus $.
- Boss day: a country-music fan keeps flipping the boombox.
- Power-ups (gold chain = speed boost, etc.).
