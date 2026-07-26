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
- **Project contact email**: currently nattflyn@gmail.com — considering LU list alias (nattfjarilar@biol.lu.se), application submitted, pending
- Get a **DOI** for the manual — Pensoft/RIO Journal or Zenodo
- validering.md step-by-step pending website UI (project filtering not yet available)
- site-specifikationer.md: exact August campaign dates to be confirmed
- Rutnät: driving directions/parking/landowner contact for Silvåkra and Björnstorp; vittjningsschema; Uppland A/B maps still show preliminary positions
- nattflyn@gmail.com renders as mailto link inconsistently — needs find-and-replace pass
- App/site screenshots need updating once ButterflyCount UI is fully translated to Swedish
- LU logos on EN assembly videos still to be confirmed consistent
- Nets for trap emptying (in production, ~2 weeks from 2026-07-24) — add note to vecko-rutin.md when distributed

## v0.4.0 — 2026-07-25

### Videos and screen recordings
- **falltyper/oversikt.md**: two new video embeds — Quad funnel/silicone dots step (`F8BcoqJBZz4`) after the main Quad assembly video; powerbank troubleshooting (`g6WUtUxQUdE`) at the end of the felsökning section
- **registrera-falla.md**: Short embed (`w4kJjqw5moU`) added at top of app-registration section; all 8 screenshots restructured to instruction-above-image with `<figure>`/`<figcaption>` to resolve caption ambiguity on desktop; spinner frame (step 7) replaced with clean settled-state frame
- **andra-observationer.md**: two Shorts added — overview (`_5r1490GXuU`) at top of page, ändra-antal (`b2fphWfQHcg`) in the app section

### Site documentation and illustrations
- **site-specifikationer.md**: `above.png` illustration (overhead drone view with compass rose) added before photo protocol table
- **ljusberakningar.md** + **ljusberakningar_diagram.jpg**: new — see v0.3.0 entry

### Styling and infrastructure
- **style.scss**: `.video-wrapper-portrait` class added (280×498px fixed, for 9:16 Shorts); `.app-figure` and `figcaption` styles added
- **_config.yml**: `version` and `version_date` variables added — version string no longer hardcoded in individual pages, use `{{ site.version }}` and `{{ site.version_date }}`

### Content
- **nyheter.md**: title changed to "Nyheter och erfarenheter"; ändringslogg filled with dated entries v0.1.0–v0.4.0; two new "När det krånglar" bullets (sensor placement, powerbank video link)

## v0.3.0 — 2026-07-24

### Rapportering — app-registrering
- **registrera-falla.md**: ny sektion med steg-för-steg-guide för registrering direkt i appen, med 8 skärmbilder extraherade från videoinspelning; Veldshop-TBD löst; CSS-klass `.app-screenshot` tillagd i style.scss

### Kontakt
- **whatsapp-och-kontakt.md**: WhatsApp-länk och länk till svensk användarguide tillagda

### Gradient och ljusberäkningar
- **gradient-lund-abisko.md**: genomgripande omskrivning — referenskarta, lokalstabell med alla 15 lokaler, förklaring av de tre kompletterande lokalerna (Gotlands Tofta, Grötö, Norrfjärden) med referenser till NAT-PoMS/SPRING, breddgradsrationale (ljusbetingelser och arbetsbelastning), uppehållstabell för nordliga lokaler
- **ljusberakningar.md**: ny fördjupningssida om beräkningsmetoden för ljusuppehåll — soldeklarationsformel, kalibrering mot Norrfjärden-observationer, diagram, osäkerhetsdiskussion, externa resurser
- **ljusberakningar_diagram.jpg**: nytt diagram, solhöjd vid astronomisk midnatt april–september för sex gradientlokaler med tröskelvärde och kalibreringspunkt markerade

### Veckorutin och site-specifikationer
- **vecko-rutin.md**: omskriven — startdatum-TBD ersatt med praktisk vägledning; säsongsslutt (30 sept); väder- och tidsinstruktioner utbyggda; Norrfjärden roterande upplägg förklarat
- **site-specifikationer.md**: LUCAS-protokoll och fotongivning tillagda; illustrationer (fallplatser-oversikt.png, habitatdok-foton.png)

## v0.2.0 — 2026-07-24

### Fälltyper — bilder och video
- Monterade fällor: fyra nya bilder (en per modell) tillagda efter respektive innehållslista
- Översiktsbild med alla fyra monterade modeller tillagd högst upp på sidan
- Monteringsvideo inbäddad för LED-Emmer Quad (SV, med LU-logotyp)
- CSS-klass `.video-wrapper` tillagd i style.scss för responsiva 16:9-inbäddningar
- Videofiler i docs/assets/videos/ med gitignore

## v0.1.0 — 2026-07-22

First substantially complete version: full manual content skeleton, site hosting and styling all live.

### Manual content — full skeleton drafted
- **index.md** — home page, front cover image, "Varför gör vi detta?" brief
- **bakgrund/oversikt.md** — EU mandate rationale, both sub-projects' purpose, tools rationale, AP-sync status, deliverables timeline
- **falltyper/oversikt.md** — all four trap models with full specs, registration naming, real unboxing photos and parts lists
- **hur-du-satter-ut/** — site-specifikationer, gradient-lund-abisko, rutnat-lund-uppsala (numbered 1–9 trap-position maps for all 4 grid squares; Lantmäteriet Topografiska Webbkartan basemaps; 250m scale bar)
- **under-experimentet/vecko-rutin.md** — weekly deploy/empty/record cycle, weather guidance
- **hur-du-rapporterar/** — registrera-falla, app-instrux (real screenshots), vad-som-raknas, andra-observationer
- **efter-inrapportering/** — validering, forvantade-resultat (placeholder)
- **kontakt-och-stod/** — whatsapp-och-kontakt, nyheter, rapportera-tekniskt-fel

### Site / hosting
- GitHub Pages, serving from `/docs` on `main`
- Custom Cayman theme override — header #C88030, cream text, project palette
- Navigation line added via `_layouts/default.html`; auto-generated sitemap `alla-sidor.md`
- Fixed Liquid syntax error from `where_exp`/`group_by` — rewritten with plain `{% for %}`/`{% unless %}`

### Cover illustration — finished
- Gradient map (gradient_karta_cover_v3.jpg) — 15 sites, colour-graded, real Sweden boundary data
- Grid-insets map (grid_insets_cover_v7.jpg) — 4-panel, real OpenFreeMap basemaps, 1km squares
- Interactive Leaflet HTML gradient map (gradient_karta_interaktiv.html)
- Trap-models watercolor illustration and moth icon
- Point shapefile of all 36 grid points (WGS84)
