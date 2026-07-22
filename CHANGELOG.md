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
- Add a **References** section (books, websites, apps cited/used throughout)
- Add an **Acknowledgements** section
- **Decide on and switch the project contact email**: currently nattflyn@gmail.com. Lars's own work email should stay reserved for scientific/academic exchanges; project participant communication should go through a dedicated address. Considering a proper LU list alias (nattfjarilar@biol.lu.se) instead of the Gmail one — this needs to be created by LU IT/admin unless Lars is granted list-admin rights himself (application submitted, pending)
- Add a link to the GitHub repo's **Issues** page for reporting website/app problems — **done, and refined further**: rather than linking straight to the external ABLE issues tracker, added a new gatekeeper page (kontakt-och-stod/rapportera-tekniskt-fel.md) that explains what that repo/issue tracker actually is, what filing an issue there requires and means (GitHub account, English, visible to the whole European user base), and asks participants to email Lars first so reports get triaged/aggregated before anything goes to the international dev team. All four existing mentions (app-instrux.md, registrera-falla.md, nyheter.md, whatsapp-och-kontakt.md) now point to this page instead of the raw GitHub link.
- Get a **DOI** for the manual as a citable product — either via a journal that supports living/dynamic documents (Pensoft ecosystem?) or via Zenodo

## v0.1.0 — 2026-07-22

First substantially complete version: full manual content skeleton, site hosting and styling all live.

### Manual content — full skeleton drafted
All sections have at least a first-pass draft:

- **index.md** — home page, front cover image, "Varför gör vi detta?" brief
- **bakgrund/oversikt.md** — EU mandate rationale, both sub-projects' purpose, tools rationale, AP-sync status, deliverables timeline (sourced from the Naturvårdsverket contract document, adapted for participants — see DECISIONS.md for the contract-vs-actual-scope note)
- **falltyper/oversikt.md** — all four trap models with full specs, registration naming, **real unboxing photos and parts lists for all four**, plus the grid-only Veldshop variant note
- **hur-du-satter-ut/** — site-specifikationer (deployment rules, lottery), gradient-lund-abisko, rutnat-lund-uppsala
- **under-experimentet/vecko-rutin.md** — weekly deploy/empty/record cycle, weather guidance
- **hur-du-rapporterar/** — registrera-falla, **app-instrux (now populated with real screenshots, no longer a stub)**, vad-som-raknas, andra-observationer (now includes website "explore data" screenshots)
- **efter-inrapportering/** — validering, forvantade-resultat (placeholder pending real pilot data)
- **kontakt-och-stod/** — whatsapp-och-kontakt, nyheter (changelog + "När det krånglar" running list)

### Known open TBDs (search each file for `[TBD:` to find them)
- Consent-text exact wording and collection mechanism (index.md)
- Registration category for the Veldshop grid-only trap variant (falltyper, registrera-falla)
- App-based (not just website) trap registration steps (registrera-falla)
- Concrete per-site start dates from trap-performance modelling (vecko-rutin)
- WhatsApp group join link (whatsapp-och-kontakt)
- **QA needed**: app screenshots (in app-instrux, registrera-falla, andra-observationer) were extracted from the old Instruktioner_nattfja_rilar_2026_v2.docx and matched to captions by document reading-order — Lars should do a quick visual pass to confirm each image is captioned correctly, a couple of the middle steps in the ButterflyCount sequence were matched with slightly less certainty than the rest
- ~~QA needed: Twincolor/Multicolor parts lists (falltyper)~~ **resolved**: confirmed the docx section titles ("Finsk modell twin" / "Finsk modell multi") were correct all along; only the internal "lampa (...)" description line inside each section had the colour name swapped, not the section itself. Manual page never displayed the erroneous colour name, so no content fix was needed beyond removing the caveat.

### Site / hosting
- **Navigation added**: Cayman has no built-in nav, so added a small "← Till startsidan · Alla sidor" line at the top of every page except the home page (via docs/_layouts/default.html), plus a new auto-generated overview page (docs/alla-sidor.md) listing every page — regenerates itself from site.html_pages, so it can't go stale. **Fixed a real build failure**: the first version used `where_exp`/`group_by` filters whose nested quotes broke GitHub Pages' locked older Liquid parser (confirmed via the Actions build log — "Liquid syntax error (line 5): Expected end_of_string but found id"); rewritten with plain `{% for %}`/`{% unless %}` only.
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
