# Changelog

All notable changes to this project are documented here.
Format: `vMAJOR.MINOR.PATCH — YYYY-MM-DD`

- **MAJOR:** Breaking change or complete redesign
- **MINOR:** New feature or significant improvement
- **PATCH:** Bug fix, data update, or minor tweak

---

## Unreleased

### Planned / backlog
- Add a **References** section (books, websites, apps cited/used throughout)
- Add an **Acknowledgements** section
- **Project contact email**: currently nattflyn@gmail.com — considering LU list alias (nattfjarilar@biol.lu.se), application submitted, pending
- Get a **DOI** for the manual — on hold, plan refined 2026-07-29: rather than a bare DOI registration (Zenodo), write a proper methods/protocol paper describing the standardised workflow (grid + gradient design, background-light-interference threshold methodology, LUCAS-adapted habitat documentation protocol), submitted to a Pensoft journal (Biodiversity Data Journal or RIO Journal) — this yields the DOI as part of publication rather than as a separate step. **Not started** — a future handover session should initiate this using the same dialogue-based drafting approach previously used for the ADMIRE Moths application (see DECISIONS.md and /areas/admire-moths.md notes). Separately: the ADMIRE Moths application itself, if accepted, should also result in its own RIO Journal submission.
- validering.md step-by-step pending website UI (project filtering not yet available)
- site-specifikationer.md: exact August campaign dates to be confirmed
- Rutnät: driving directions/parking still TBD for Skåne A/B (landowner contact now added); vittjningsschema; Uppland A/B still need real registered GPS trap positions (currently uses an evenly-spaced grid derived from the official 1km squares, not placeholder/preliminary data — see v0.9.0)
- App/site screenshots need updating once ButterflyCount UI is fully translated to Swedish
- LU logos on EN assembly videos still to be confirmed consistent
- Nets for trap emptying (in production, ~2 weeks from 2026-07-24) — add note to vecko-rutin.md when distributed

## v0.11.0 — 2026-07-29

### English translation
- Full English translation of the manual added under a new `/en/` section,
  mirroring the entire Swedish page structure 1:1 (19 pages: index, om-manualen,
  bakgrund, falltyper, all four hur-du-satter-ut pages, all four
  hur-du-rapporterar pages, both efter-inrapportering pages, all four
  kontakt-och-stod pages, vecko-rutin, alla-sidor).
- New EN/SV language toggle in the site header (docs/_layouts/default.html),
  plus dual home/alla-sidor links in the page-top-nav breadcrumb.
- EU-Lex regulation links in bakgrund.md swapped to their `/EN/` equivalents
  on the English page.
- English feedback form added (separate from the Swedish Google Form/sheet
  tracker) — linked from synpunkter.md and whatsapp-och-kontakt.md.

### PDF export
- `build_pdf.py` now builds both language editions in one run
  (`nattfjarilar-manual.pdf` and `nattfjarilar-manual-en.pdf`), each with its
  own generated cover page. English download links on index.md/alla-sidor.md
  now point to the English-specific PDF instead of the shared Swedish one.

### Fixes
- Corrected several English video embeds in falltyper/oversikt.md that were
  pointing at nonexistent video IDs — now use the same real IDs as the
  Swedish page (each video already carries both language caption tracks;
  viewers select their preferred subtitle language manually via the CC
  button, since YouTube's `cc_lang_pref` parameter proved unreliable at
  forcing a specific language).
- Various English terminology refinements: "put out"/"putting out" vs.
  "deploying" (matching the two registers "sätta ut" spans in Swedish but
  English distinguishes), and "background light interference" instead of
  the earlier, misleadingly emotional "disturbing background light".

## v0.10.0 — 2026-07-28

### PDF export
- Manualen kan nu laddas ner som en utskriftsvänlig PDF. Ny lokal byggprocess
  (`build_pdf.py`, körs manuellt vid behov, ingår inte i CI) renderar samtliga
  sidor via headless Chromium med en dedikerad utskrifts-stylesheet, genererar
  ett titelblad (titel, version, kontaktuppgifter), och slår ihop allt till en
  enda PDF.
- Ny utskrifts-CSS i style.scss: döljer sidhuvud/navigering, visar
  videoinbäddningar som klickbara länkar istället för iframes (kräver
  `data-video-url`-attribut, tillagt på samtliga 8 videoinbäddningar),
  begränsar bildstorlek för att undvika för stora bilder och udda sidbrytningar.
- Nedladdningslänk med förklarande text tillagd på index.md och alla-sidor.md:
  förtydligar att PDF:en är en ögonblicksbild och att viss layout/videolänkar
  fungerar annorlunda i utskrift jämfört med webbsidan.
- Filnamnet är medvetet oversionerat (`nattfjarilar-manual.pdf`) så
  nedladdningslänken aldrig blir inaktuell vid en versionsuppdatering.

## v0.9.1 — 2026-07-28

### YouTube-videor: undertextproblemet löst
Efter flera försök: alla fem svenska videor (LED-Emmer, Quad, Quad-tratt/silikonprickar, EntoLight, powerbank-felsökning) laddades om med nya YouTube-ID:n och riktiga undertextspår istället för inbrända undertexter, vilket var den faktiska orsaken till att iframes laddade extremt långsamt eller misslyckades helt ("An error occurred"-fel). `referrerpolicy="strict-origin-when-cross-origin"` tillagd på alla videoinbäddningar. SV-inbäddningar använder nu `cc_load_policy=1&cc_lang_pref=sv` (undertexter på som standard) istället för tidigare `cc_load_policy=0`.
- YouTube-kanalen flyttad till @dagfjarilar
- **andra-observationer.md**: `referrerpolicy="strict-origin-when-cross-origin"` tillagd på de två kvarvarande Shorts-inbäddningarna (ändra antal, se och ändra observationer) — nu konsekvent med övriga videoinbäddningar

### Terminologi och länkar
- **kärnlokaler → huvudlokaler**: kvarvarande förekomst åtgärdad
- **nattflyn@gmail.com**: find-and-replace-pass genomförd, mailto-länkar renderas nu konsekvent

### Övrigt
- **om-manualen.md**: rubriken "Bidragsgivare" ändrad till "Bidrag från"
- Namnmiss på kartorna (rutnät) fixad

## v0.9.0 — 2026-07-27

### Rutnät: fällpositionskartor återinförda, säkerhetsförskjutna
Löser det som v0.8.0 loggade som ofullständigt (fel upplösning, ingen fungerande metod).

- **Ny metod för skalstock**: istället för att lita på QGIS egen skalstocksdekoration (som visade fel mått), detekteras den befintliga 1×1 km-rutan direkt i varje bild via bildanalys (letar efter långa sammanhängande mörka linjer, till skillnad från text som bryts upp i korta segment) — ger en exakt pixel-till-meter-kalibrering per bild utan koordinater eller projektion inblandat. Alla fyra bilder gav samma kalibrering (~2057 px = 1000 m), vilket bekräftar att QGIS-exporterna var konsekventa. Skalstocken (250 m) ritas därefter direkt utifrån detta mått.
- **Beskurna** till samma proportioner som originaldesignen (rutan upptar ~42% av bildbredden) och nedskalade till 1540×1540 px.
- **Uppland A/B**: löste kvarvarande missanpassning mellan 3×3-rutnätet och 1×1 km-rutan genom att generera nya, jämnt fördelade punkter direkt från rutans egna fyra hörn (bilinjär interpolering, helt inom SWEREF99TM, ingen lat/lon-konvertering) istället för att felsöka det tidigare separat förskjutna punktlagret. Rutan och de nya punkterna är därmed garanterat i linje, eftersom punkterna är matematiskt härledda ur rutan.
- **rutnat-lund-uppsala.md**: sidan återinförd med anonymiserade platsnamn (Skåne A/B, Uppland A/B — inga riktiga bynamn) och de säkerhetsförskjutna kartorna (`skane-a-public.jpg`, `skane-b-public.jpg`, `uppland-a-public.jpg`, `uppland-b-public.jpg`). Ny sektion **Markägarkontakter** tillagd (Skåne via Lars, Uppland via kontaktpersonen på SLU angiven i sidan). Förtydligande mening tillagd om varför kartornas geografiska placering är förskjuten.
- **Bokföring**: de ursprungliga, oförskjutna bilderna med de faktiska positionerna flyttade till `docs/assets/images/precise-maps/` (döpta om till `skane-a/b-precise.jpg`, `uppland-a/b-precise.jpg`) och tillagda i `.gitignore` — behålls för Lars egen bokföring, pushas aldrig till det publika repot/webbplatsen.

## v0.8.0 — 2026-07-27 (planned, not yet pushed)

### Attempted (incomplete)
- **rutnat-lund-uppsala.md position maps**: attempted displaced versions for all four sites
  (Skåne A/B, Uppland A/B) — multiple approaches tried but none successfully reproduced
  the original map style at the required resolution. Maps remain removed from the public
  page. See DECISIONS.md and HANDOVER.md for the correct approach for next session.

### Confirmed actual GPS positions
- Skåne A (Silvåkra): 9 actual GPS positions matched to grid numbers 1-9 (confirmed)
- Skåne B (Björnstorp): 9 actual GPS positions matched to grid numbers 1-9 (confirmed)
- Uppland A/B: ideal positions as placeholder, actual GPS still needed

### QGIS displacement scripts added to repo root
- Skane_45_topo_displaced.py (1km W + 500m S)
- Skane_96_topo_displaced.py (1km E + 500m S)
- Uppland_A_topo_displaced.py (2km E + 500m S)
- Uppland_B_topo_displaced.py (1km E + 500m S)

## v0.7.0 — 2026-07-26

### Ny sida: Om manualen
- **om-manualen.md**: ny sida med bidragsgivare (Harriet Arnberg, Amanda Ernstsson,
  Ana Teodora Ştefan), finansiering (NV-26-076242), projektpartners (LU, SLU Ekologi,
  SLU Artdatabanken) och AI-ansvarsfriskrivning
- Bidragsgivarkreditering tillagd på index.md direkt under omslagsbilden
- Länk till om-manualen.md tillagd i sidfoten på index.md

### Synpunkter och feedback
- **synpunkter.md**: ny sida i kontakt-och-stod/ med inbäddad publik Google Sheets-vy
  (Publik vy-flik, gid=502981035) med inkomna synpunkter och status
- Google Form (https://forms.gle/5Vrf68vXGjDm9eEv9) med fem kategorier:
  appen, hemsidan, fällutrustning, manualen, övrigt
- Formulärlänk tillagd i whatsapp-och-kontakt.md, rapportera-tekniskt-fel.md och index.md
- Status-dropdown: Ny, Under behandling, Åtgärdad, Vidarebefordrad, Noterat ingen åtgärd

## v0.6.0 — 2026-07-26

### Videor och shorts
- **falltyper/oversikt.md**: Quad-tratt-video (F8BcoqJBZz4) och powerbank-video
  (g6WUtUxQUdE) tillagda
- **registrera-falla.md**: Short-video (w4kJjqw5moU) + figcaptions + instruktion-före-bild
- **andra-observationer.md**: två Shorts — översikt (_5r1490GXuU) och ändra antal
  (b2fphWfQHcg); appsektionen nu före hemsidessektionen

### Infrastruktur
- **style.scss**: .video-wrapper-portrait och .app-figure/figcaption tillagda
- **_config.yml**: version och version_date variabler ({{ site.version }},
  {{ site.version_date }}) — versionssträngen hårdkodas inte längre i enskilda sidor

### Övrigt
- **nyheter.md**: platshållarmening borttagen, ändringslogg ifylld, länktext uppdaterad
- **site-specifikationer.md**: above.png illustration tillagd före fotoprotokolltabell
- **reg-steg7-lampa-sparad.jpg**: spinner-bild ersatt med ren frame (t=42s)

## v0.5.0 — 2026-07-26

### Korrekturläsning och terminologi
- Genomgripande korrekturläsningspass av alla sidor
- vittjning/vittja → tömning/tömma av fällan genomfört i berörda sidor
- Intro-mening i falltyper/oversikt.md korrigerad: alla fyra fällmodeller används
  parallellt per gradientlokal (inte en fälla per lokal som felaktigt angavs)
- bakgrund/oversikt.md omdöpt till bakgrund/bakgrund.md; interna länkar uppdaterade
- rutnat-lund-uppsala.md: fällpositionskartor borttagna i avvaktan på diskussion om
  offentlig publicering av exakta positioner; TBDs och e-posttypo åtgärdade
- ljusberakningar.md: omskriven med ny vinkel — standardisering av störande
  bakgrundsljus snarare än "ljusuppehåll"; populärvetenskaplig ton
- forvantade-resultat.md: språkligt polerad
- om-manualen.md: heading "Ansvarig utgivare" ändrad till "Framtagen av"
- Alla mailto-länkar för nattflyn@gmail.com genomgångna och korrigerade

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
