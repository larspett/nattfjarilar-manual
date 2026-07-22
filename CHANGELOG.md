# Changelog

All notable changes to this project are documented here.
Format: `vMAJOR.MINOR.PATCH — YYYY-MM-DD`

- **MAJOR:** Breaking change or complete redesign
- **MINOR:** New feature or significant improvement
- **PATCH:** Bug fix, data update, or minor tweak

---

## Unreleased

### Planned / backlog
- Add an option to export/print the whole site as a PDF manual (discussed early on, for participants who prefer offline/print over the website)
- Full English translation of the site as a parallel version
  - Note: EU-Lex regulation links (used in Bakgrund) switch language by swapping `/SV/` for `/EN/` in the URL, e.g. `.../legal-content/EN/TXT/HTML/?uri=OJ:L_202401991` — same pattern for both cited regulations

## v0.1.0 — 2026-07-22

First substantially complete version: full manual content skeleton, site hosting and styling all live.

### Manual content — full skeleton drafted
All sections have at least a first-pass draft:

- **index.md** — home page, front cover image, "Varför gör vi detta?" brief
- **bakgrund/oversikt.md** — EU mandate rationale, both sub-projects' purpose, tools rationale, AP-sync status, deliverables timeline (sourced from the Naturvårdsverket contract document, adapted for participants — see DECISIONS.md for the contract-vs-actual-scope note)
- **falltyper/oversikt.md** — all four trap models with full specs, registration naming, powerbank troubleshooting, plus the grid-only Veldshop variant note
- **hur-du-satter-ut/** — site-specifikationer (deployment rules, lottery), gradient-lund-abisko, rutnat-lund-uppsala
- **under-experimentet/vecko-rutin.md** — weekly deploy/empty/record cycle, weather guidance
- **hur-du-rapporterar/** — registrera-falla, app-instrux (stub, needs screenshots), vad-som-raknas, andra-observationer
- **efter-inrapportering/** — validering, forvantade-resultat (placeholder pending real pilot data)
- **kontakt-och-stod/** — whatsapp-och-kontakt, nyheter (changelog + "När det krånglar" running list)

### Known open TBDs (search each file for `[TBD:` to find them)
- Consent-text exact wording and collection mechanism (index.md)
- Registration category for the Veldshop grid-only trap variant (falltyper, registrera-falla)
- App-based (not just website) trap registration steps (registrera-falla)
- Concrete per-site start dates from trap-performance modelling (vecko-rutin)
- app-instrux.md needs actual numbered screenshots/short videos
- WhatsApp group join link (whatsapp-och-kontakt)

### Site / hosting
- **Hosting**: GitHub Pages, serving from `/docs` on `main` — repo also holds DECISIONS.md/CHANGELOG.md for project bookkeeping
- **Styling**: custom Cayman theme override (assets/css/style.scss) — header background solid accent orange/caramel #C88030, header text light/cream, links/buttons in the project's brown/orange palette
- **Home page**: finished front-cover composite (assets/images/framsida.jpg) displayed in main content below the header; author byline with email ("Lars B. Pettersson, Biologiska institutionen, Lunds universitet · lars.pettersson@biol.lu.se") added inside the header banner via a minimal layout override (docs/_layouts/default.html)
- Known minor cosmetic issue, not being chased further: byline font doesn't scale with Cayman's desktop breakpoint (looks fine on phone, small relative to the title on wide desktop screens)

### Cover illustration — finished
- Gradient map (gradient_karta_cover_v3.jpg) — 15 sites on real Sweden boundary data, colour-graded south-to-north by rank, ideal-latitude reference bands, sticker colour palette
- Grid-insets map (grid_insets_cover_v7.jpg) — 4-panel surround layout (Skåne 45/96, Uppland A/B), each with a real cropped OpenFreeMap Bright basemap, 1km reference squares
- Interactive Leaflet HTML gradient map (gradient_karta_interaktiv.html) — for the online manual, separate from the print cover
- Trap-models watercolor illustration and flat-line moth icon — received finished from Lars
- Front cover composite — assembled and exported by Lars from his own layout tool (cover_illustration_manual_v2.jpg, later updated with more padding)
- Point shapefile of all 36 grid points (moth_grid_points shapefile, WGS84) exported for GIS use
