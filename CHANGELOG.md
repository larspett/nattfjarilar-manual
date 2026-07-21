# Changelog

All notable changes to this project are documented here.
Format: `vMAJOR.MINOR.PATCH — YYYY-MM-DD`

- **MAJOR:** Breaking change or complete redesign
- **MINOR:** New feature or significant improvement
- **PATCH:** Bug fix, data update, or minor tweak

---

## Unreleased

### Manual content
- Manual skeleton drafted: index + Bakgrund, Fälltyper, Sätta ut fällor (deployment), Under experimentet, Hur du rapporterar, Efter inrapportering, Kontakt och stöd
- **Hosting decided: GitHub Pages, serving from `/docs` on `main`** — repo also holds DECISIONS.md/CHANGELOG.md for project bookkeeping
- Trap model specs finalized for all four models (LED-Emmer standard, LED-Emmer 2.0 Quad, EntoLight Twincolor, EntoLight Multicolor), including registration naming convention and powerbank troubleshooting
- Deployment rules finalized: 4 sites ≥50m apart per gradient location, trap type assigned by lottery and fixed for the season
- Gradient site list finalized: 15 sites, Revinge to Abisko (incl. 2.5, 3a/3b, 10a/10b sub-numbering)
- Reporting/taxonomy scope decided: macromoths mandatory, micro/other groups optional, Dyntaxa taxonomy mismatch noted as a known issue
- Bakgrund section still needs final why/importance/urgency text (source: Naturvårdsverket document, not yet drafted)

### Cover illustration (finished)
- Gradient map (gradient_karta_cover_v3.jpg) — 15 sites on real Sweden boundary data, colour-graded south-to-north by rank, ideal-latitude reference bands, sticker colour palette — **confirmed final**
- Grid-insets map (grid_insets_cover_v7.jpg) — 4-panel surround layout (Skåne 45/96, Uppland A/B), each with a real cropped OpenFreeMap Bright basemap, 1km reference squares, colour-matched to the gradient map — **confirmed final**
- Interactive Leaflet HTML gradient map (gradient_karta_interaktiv.html) — for the online manual, separate from the print cover
- Trap-models watercolor illustration and flat-line moth icon — both received finished from Lars
- Front cover composite — assembled and exported by Lars from his own layout tool (cover_illustration_manual_v2.jpg) — **confirmed final**
- Point shapefile of all 36 grid points (moth_grid_points shapefile, WGS84) exported for GIS use

## v0.1.0 — YYYY-MM-DD
- Initial version
