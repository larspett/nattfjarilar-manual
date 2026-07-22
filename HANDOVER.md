# Handover: Pilotprojekt nattfjärilar 2026 — manual project

If you're a fresh Claude session picking this up: read this file, then `DECISIONS.md` and `CHANGELOG.md` in this same repo root. Together those three are the full continuity record. Don't assume you have prior memory of this project even if you do, this file is the ground truth.

## What this project is

A field manual for a Swedish moth-monitoring pilot (2026), covering two sub-projects: **Landskapseffekter** (3×3 trap grids in Lund and Uppsala) and **Latitudgradient** (15 sites Lund–Abisko, four trap models compared). Run by Lars B. Pettersson, Biologiska institutionen, Lunds universitet.

## Where everything lives

- **The manual itself**: `docs/` in this repo, built with Jekyll (Cayman theme + custom overrides), served live at https://larspett.github.io/nattfjarilar-manual/
- **`DECISIONS.md`**: why things are the way they are, read this before re-litigating a design choice
- **`CHANGELOG.md`**: current status, what's drafted, what's still open (search for "TBD" across `docs/` for the authoritative live list, `CHANGELOG.md`'s list can lag slightly behind the actual files)
- **Cover illustrations** (gradient map, grid-insets map, trap illustration, moth icon, all finished) live as image assets under `docs/assets/images/`

## How Lars works (worth knowing before diving in)

- Local repo lives inside **Box Drive** (Box-Box CloudStorage sync), which has caused file-drift issues with piecemeal handoffs. **Always hand off a full project zip** (repo root + `docs/`), not individual files, unless he explicitly asks for just one small file.
- He wants the **ready-to-paste terminal commands** (`cd` / `unzip` / `git add` / `commit` / `push`) supplied alongside every zip, so he isn't reconstructing them each time.
- He's comfortable in Terminal and with git, but hit real friction with GitHub Pages/Jekyll specifics (Liquid syntax errors, build failures) that needed debugging via the Actions tab logs, not guesswork.
- Prefers `ljusmodul` and `vingar` as the standard terms for the trap's light component and its mounting fins, not "lampa."
- Avoids Microsoft software generally (bloat/lock-in concerns); uses Typora for markdown.

## Known technical gotchas (don't relearn these the hard way)

- **GitHub Pages runs an old, strict Liquid parser** (Jekyll 3.10.0 / github-pages gem). Avoid `where_exp`, `group_by`, and filters with nested quotes, they've caused real build failures here. Stick to plain `{% for %}` / `{% if %}` / `{% unless %}` with simple filters (`relative_url`, `default`, `first`).
- The site has a **custom layout override** (`docs/_layouts/default.html`) for: the header author byline, the front-cover image placement (main content, NOT inside the header banner, that was tried and explicitly reverted), and a site-wide top-of-page nav line. Any layout edit should touch only what's intended, this file has a history of scope-creep mistakes from over-broad edits.
- `docs/alla-sidor.md` is a **self-updating sitemap** (uses `site.html_pages`), don't hand-maintain a page list elsewhere.
- Real basemap images (OpenFreeMap for the cover, Lantmäteriet Topografiska Webbkartan for the in-manual rutnät maps) are cropped precisely from raw QGIS exports using their `.jgw` world files, see the DECISIONS.md entries on cover illustration for why real basemaps replaced illustrative ones (it solved a long-running "looks too pale" styling problem that many CSS-only attempts failed to fix).

## Recommended tooling going forward

Given how much of the friction here was file/git mechanics rather than the actual content work, **Claude Code** (terminal or desktop) is likely a better fit than continuing pure chat handoffs for anything touching the repo directly, it can read/write files and run git commands in place, eliminating the zip round-trip entirely. Chat remains the right tool for the iterative design/content review itself (map crops, wording, colour choices), that part doesn't benefit from more autonomy, it benefits from fast back-and-forth.

## Current status (see CHANGELOG.md for the authoritative version)

All 15 manual content pages have real first-pass content. Front cover is finished. Site is live with navigation, custom styling, and real photos/maps throughout Fälltyper and the rutnät pages. Remaining open items are small (a few TBDs, a backlog list of nice-to-haves like a PDF export option, English translation, and a DOI via Pensoft's RIO Journal), nothing structural is unfinished.
