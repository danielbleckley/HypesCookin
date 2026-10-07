# HYPE'S COOKINN 🐟🎤

Mobile-web arcade game. Live at https://danielbleckley.github.io/HypesCookin/ (GitHub Pages).
Source game: `game/index.html`. Shareable single-file build: `HypesCookinn.html` / `index.html`
(art base64-inlined). See `README.md` and `game/README.md` for tuning knobs.

## Run
- `cd game && python3 -m http.server 8753` → http://localhost:8753
- After changing `game/assets/`, rebuild the inlined art: `cd game && python3 inline_assets.py` (needs Pillow).
- Keep the root `index.html` / `HypesCookinn.html` in sync with `game/index.html` when gameplay changes.

## Rules for every session (desktop, web, or phone)
- **`main` is production.** GitHub Pages publishes `main` to the public game link. Never push to `main` directly — work on a branch and open a pull request with a short, plain-English summary of what changed and how to check it. Buddy reviews and merges them, often from a phone.
- Before opening the PR, run: `python3 -c "import html.parser,sys; html.parser.HTMLParser().feed(open('game/index.html').read())"` and fix anything it breaks.
- Never commit secrets or `.env` files. Production env vars live in the Render dashboard (see `render.yaml`, `sync: false` keys).
- Keep commits small and titled in plain English (what the user will notice), matching the existing git log.
