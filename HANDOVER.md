# Handover — Pilotprojekt nattfjärilar 2026 manual

Read this first in any new session. It is the single source of truth for continuity.
Detailed record lives in DECISIONS.md and CHANGELOG.md at the repo root.

---

## What this project is

A field manual for a 2026 Swedish moth monitoring pilot, hosted as a public Jekyll/GitHub
Pages website at https://larspett.github.io/nattfjarilar-manual/. ~15 participants run
light traps at sites across Sweden (grid sub-project in Lund/Uppsala; 15-site
Lund-to-Abisko latitude gradient). Current version: **v0.7.0 (2026-07-26)**.

Lars B. Pettersson (lars.pettersson@biol.lu.se), Biologiska institutionen, Lunds
universitet. Contributors: Harriet Arnberg, Amanda Ernstsson, Ana Teodora Ştefan (all LU).
Funded by Naturvårdsverket, contract NV-26-076242.

---

## Site is live and essentially complete

All ~15 pages have real content. Proofreading pass completed 2026-07-26.
Repo: github.com/larspett/nattfjarilar-manual (public)

**Page inventory:**
```
index.md, om-manualen.md, alla-sidor.md
bakgrund/bakgrund.md
falltyper/oversikt.md
hur-du-satter-ut/site-specifikationer.md, gradient-lund-abisko.md,
  ljusberakningar.md, rutnat-lund-uppsala.md
under-experimentet/vecko-rutin.md
hur-du-rapporterar/registrera-falla.md, app-instrux.md,
  vad-som-raknas.md, andra-observationer.md
efter-inrapportering/validering.md, forvantade-resultat.md
kontakt-och-stod/whatsapp-och-kontakt.md, rapportera-tekniskt-fel.md,
  nyheter.md, synpunkter.md
```

**Infrastructure:**
- Jekyll/Cayman, GitHub Pages from /docs on main
- Version: `{{ site.version }}` / `{{ site.version_date }}` in docs/_config.yml
- CSS: docs/assets/css/style.scss — palette #C88030/#63533F/#F6EADA
- CSS classes: `.video-wrapper` (16:9), `.video-wrapper-portrait` (9:16 280×498px),
  `.app-screenshot` (max 260px), `.app-figure`/figcaption
- DO NOT use where_exp/group_by in Liquid — breaks GitHub Pages' old Liquid parser

---

## Open items — most urgent first

### 1. Rutnät position maps (INCOMPLETE — maps currently removed from public page)

The original maps (silvakra.jpg, bjornstorp.jpg, uppland-a.jpg, uppland-b.jpg) showed
exact trap GPS positions — a theft risk. They need to be replaced with versions showing
DISPLACED positions on blurred/displaced basemaps, matching the original style exactly.

**What the original maps look like (THIS IS THE TARGET):**
- 1540×1540px
- Background: Lantmäteriet Topografisk Webbkarta, ~1m/px (NOT the wide 5.5m/px exports)
- Orange circles (#C88030): actual GPS positions, radius ~35px at 1540px, white border,
  numbered 1-9, font size ~28-30pt
- White dots: ideal/planned grid positions, radius ~10px, dark grey border for visibility
- Grey 1km² box outline: from edge of ideal grid positions + margin
- Scale bar: 250m = ~167px at 1540px (= ~11% of image width)
- 1km box = ~43-45% of image width (NOT 72% — Lars's 72% measurement was of the
  marker cluster, not the box outline)
- Thin brown border around whole image

**What went wrong in this session:**
Multiple attempts failed due to scale/resolution mismatch. The wide QGIS tile exports
(5.4-6.1m/px at 2166×796px or 3080×3080px) cannot reproduce the ~1m/px resolution of
the original maps when cropped to match the original geographic coverage. Every attempted
crop+upscale produced either wrong scale or pixelated background.

**The correct approach for next session:**
Lars needs to export from QGIS at the SAME resolution as the original maps:
- In QGIS, use the SAME Python script as the original (Skane_45_topo.py etc.) but with
  the displaced coordinates (see Skane_45_topo_displaced.py etc. at repo root)
- Export: Project → Import/Export → Export Map to Image
- Set output to exactly 1540×1540px (matching original)
- Ensure Lantmäteriet Topografisk Webbkarta is the active basemap
- Export ONCE per site with decoration layers OFF (markers/decorations removed)
- Then Claude draws orange circles, white dots, box and scale bar on top in Python

**Displacement amounts (apply to QGIS Python scripts):**
- Skåne A (Silvåkra): 1km West + 500m South → new centre lon=13.443195, lat=55.690476
- Skåne B (Björnstorp): 1km East + 500m South → new centre lon=13.447993, lat=55.618321
- Uppland A: 2km East + 500m South → new centre lon=17.769629, lat=59.914882
- Uppland B: 1km East + 500m South → new centre lon=18.029761, lat=59.961888

**Coordinate data available:**
- Ideal positions (white dots, all 4 sites): docs/assets/images/rutnat/ideal_positions_grid.csv
  (also in uploads from this session)
- Actual GPS (orange circles): Skåne A and B confirmed (see DECISIONS.md); Uppland A/B
  still placeholder (Lars needs to provide)
- Skåne A actual (9 positions, already matched 1-9): see DECISIONS.md
- Skåne B actual (9 positions, already matched 1-9): see DECISIONS.md

**QGIS displacement scripts:** Skane_45_topo_displaced.py, Skane_96_topo_displaced.py,
Uppland_A_topo_displaced.py, Uppland_B_topo_displaced.py — all at repo root.

**When correct 1540×1540 basemaps are available**, use this drawing code structure:
```python
# R = 6378137.0
# def wgs84_to_3857(lon, lat):
#     x = lon * math.pi/180 * R
#     y = math.log(math.tan(math.pi/4 + lat*math.pi/360)) * R
#     return x, y
# read_jgw → px_size, x0, y0
# coord_to_px: apply dlon/dlat to displaced coords, convert to pixel via JGW
# Draw: box (grey, width=2), white dots (r=10, dark outline), orange circles (r=35, font=28pt)
# Scale bar: 250m = int(250/px_size) px before any scaling
```

### 2. Pending smaller items
- **validering.md**: step-by-step pending website UI (project filtering not yet available)
- **Arnberg & Pettersson 2026**: add link in app-instrux.md once correct doc on LU Research Portal
- **Nets for trap emptying**: arriving ~Aug 2026, add note to vecko-rutin.md
- **August habitat documentation campaign**: confirm exact dates, update site-specifikationer.md
- **Uppland A/B actual GPS positions**: Lars to provide, then regenerate those two maps
- **forvantade-resultat.md**: link to live data once pilot data arrives
- **Videos**: re-export without burnt-in subtitles, upload .srt to YouTube; temp fix
  `?cc_lang_pref=&cc_load_policy=0` already applied to all embed URLs
- **kärnlokaler → huvudlokaler**: one occurrence in gradient-lund-abisko.md
- **rutnat-lund-uppsala.md**: maps removed pending displaced versions; page has placeholder text

### 3. Longer-term backlog
- English translation (EU-Lex links: swap /SV/ → /EN/)
- PDF export
- DOI via RIO Journal (Pensoft)
- References and Acknowledgements sections
- Project email LU list alias (nattfjarilar@biol.lu.se, pending admin rights)

---

## YouTube videos

Assembly (16:9, `.video-wrapper`):
- LED-Emmer SV: GrrSlT9ah-M | EN: tYH48SZjwUo
- LED-Emmer Quad SV: hnr4Ww46mHg | EN: 62XC7lHacvI
- LED-Emmer Quad funnel SV: F8BcoqJBZz4 | EN: OJanLABY1RU
- EntoLight SV: 7UC9A0au6N8 | EN: a891Pv0Imhc
- Powerbank SV: g6WUtUxQUdE | EN: cDKbjC3L4cM

Screen recording Shorts (9:16, `.video-wrapper-portrait`):
- Registrera lokal: w4kJjqw5moU
- Se och ändra observationer: _5r1490GXuU
- Ändra antal: b2fphWfQHcg

Feedback form: https://forms.gle/5Vrf68vXGjDm9eEv9
Public embed (synpunkter.md): Google Sheets Publik vy tab, gid=502981035

---

## Lars's working preferences

- Avoids em dashes (AI detection signal), Microsoft tools
- Prefers minimal-intervention edits with clear reasoning
- Terminology: ljusmodul, vingar, tömning av fällan (not vittjning)
- Palette: cream #F6EADA, brown #63533F, accent #C88030
- Primary Swedish regulatory sources over secondary
