# Design & Technical Decisions

This file logs significant decisions made during development, with rationale.
Update it whenever a non-obvious choice is made.

## Format
**YYYY-MM-DD — Decision title**
- **What:** Brief description of the decision
- **Why:** Rationale, alternatives considered
- **Impact:** What this affects

---

## Manual format and platform

**2026 — Manual delivered as a website, not GitHub/MkDocs or a static PDF**
- **What:** The participant manual is a website with versioning and section-jumping, with PDF export available for those who want it.
- **Why:** Went through GitHub/MkDocs → plain PDFs → back to a website. Rejected GitHub/MkDocs since the ~15-person audience doesn't need Git literacy or infrastructure at that scale. Rejected PDF-only since a 20+ page document doesn't get read; section-jumping matters more than offline access here.
- **Impact:** No GitHub repo, no Mailchimp integration, no separate FAQ database, no QR codes for now — all rejected as infrastructure the audience size doesn't justify.

**2026 — Manual structure is timeline-based, not split by sub-project**
- **What:** Structure follows Bakgrund → Before the experiment → During → After data submission → Kontakt/Nyheter, rather than having fully separate "grid" and "gradient" sections.
- **Why:** Only the deployment/site-selection content genuinely differs between the grid and gradient sub-projects; everything else (trap types, reporting, taxonomy scope) is shared. A timeline split matches how a participant actually uses the manual (once at the start, repeatedly during the season) better than a project split would.
- **Impact:** Deployment section has a gradient subsection (longer, ~75-80% of content) and a grid subsection (short, since it's run by two experienced people).

**2026 — No standalone FAQ; "När det krånglar" + "senaste erfarenheterna" instead**
- **What:** Troubleshooting content lives as a running, dated list tied to the Nyheter/changelog page, not a separate static FAQ.
- **Why:** Static FAQs get less attention over time; a page that's visibly "alive" (tied to update history) holds attention better for a small, engaged group.

## Project design and deployment rules

**2026 — Trap type is randomly assigned per site and fixed for the season**
- **What:** At each gradient site, 4 trap locations are chosen ≥50m apart, then trap type is assigned to each location by drawing lots. That assignment is fixed for the whole season.
- **Why:** Protects the experimental design (site×trap-type confounding) against well-intentioned participant "improvements" mid-season.
- **Impact:** Needs strong communication in the manual.

**2026 — Artportalen sync framed as a goal, not a promise**
- **What:** Manual tells participants the concrete, deliverable fact (data can always be exported and manually imported to Artportalen) and frames automatic sync as a future aim, not a current feature.
- **Why:** Automatic sync requires both participant consent and Artdatabanken's approval, which hasn't been granted.

**2026 — Participant contact/address list kept out of the manual entirely**
- **What:** A separate, participant-only document handles names/addresses/contact sharing consent; the manual itself never includes this.
- **Why:** Keeps the manual shareable/public-facing without a privacy dependency.

## Cover illustration

**2026-07 — Sweden outline sourced from real boundary data, not hand-drawn**
- **What:** Switched from a ~50-point freehand approximation to the actual Natural Earth boundary (3,388-point mainland + real islands).
- **Why:** The hand-drawn version read as an unrecognizable blob.
- **Impact:** Both the gradient map and grid-insets map use this same boundary data.

**2026-07 — Grid-insets map uses real OpenFreeMap basemap images**
- **What:** Each of the four grid insets shows an actual cropped OpenFreeMap Bright export as its background.
- **Why:** Real map tiles carry genuine visual density that styling tweaks on a blank background can't replicate. This was the fix that resolved a long-running "too pale" problem.
- **Impact:** Front cover uses grid_insets_cover_v7.jpg as final.

**2026-07 — Front cover is 4 independently-produced pieces assembled by Lars**
- **What:** Moth icon, gradient map, grid-insets map, and trap-illustration are each finished separately; Lars assembles and exports the final composite himself.
- **Why:** Exporting from the source layout tool is more reliable than reconstructing proportions from a screenshot.

## Manual hosting

**2026-07 — Manual is hosted on GitHub Pages**
- **What:** The GitHub repo hosts the manual's markdown source (in `/docs`) and is also where DECISIONS.md and CHANGELOG.md live. GitHub Pages configured to serve from `main` branch, `/docs` folder.
- **Why:** GitHub Pages' built-in Jekyll processing (zero local setup, auto-builds on push) satisfies the original requirement (versioned website with section-jumping) without contradicting the earlier "keep it simple" reasoning.
- **Impact:** Each markdown file needs minimal Jekyll front matter. Relative `.md` links work via `jekyll-relative-links`.

**2026-07 — Video files never go in git; hosted on YouTube instead**
- **What:** All MP4 assembly videos are hosted as public YouTube videos and embedded via iframe. Local source files live in `docs/assets/videos/` but are gitignored. The 100MB GitHub file size limit makes large MP4s impossible; even files under the limit cause history bloat.
- **Why:** Learned the hard way when a 238MB EntoLight video caused a rejected push. YouTube is the right tool for video hosting.
- **Impact:** `docs/assets/videos/*_LU.mp4` is gitignored. EN edition videos stay local-only until that edition is underway.

**2026-07 — Version managed via _config.yml variables**
- **What:** `version` and `version_date` are set in `docs/_config.yml` and referenced in pages as `{{ site.version }}` and `{{ site.version_date }}`.
- **Why:** Eliminates the need to hunt and update hardcoded version strings in multiple markdown files on each release.
- **Impact:** Version bumps require only a single edit in `_config.yml`.

## Project scope: manual numbers vs. the funder contract

**2026-07 — Manual uses the actual expanded scope (15 gradient sites, 4 trap models)**
- **What:** The signed contract with Naturvårdsverket states 10 gradient localities and 3 trap types. The manual reflects 15 sites and 4 trap models throughout.
- **Why:** After the contract was drafted, a follow-up meeting expanded the gradient and added a 4th trap model; the budget was increased but the contract text was never revised.

**2026-07 — Artportalen sync remains "goal, not promise" despite the contract stating it as settled**
- **What:** The contract document states "validated data is synced to Artportalen" as if already agreed. This is NOT accurate — Artdatabanken has not committed.
- **Why:** Confirmed directly by Lars; the contract text on this point is aspirational/outdated.

## Darkness window calculations

**2026-07 — Calibrated against Norrfjärden field observations, not purely astronomical**
- **What:** The no-trap period for northern sites is calculated using a threshold midnight solar elevation of −2.73°, calibrated against a volunteer's field observations at Norrfjärden (65.42°N): trapping viable to 31 May, not viable from around midsommar.
- **Why:** A purely astronomical threshold (e.g. nautical twilight at −12°) doesn't match how moths actually respond to light conditions. The empirical calibration grounds the calculation in real field experience.
- **Impact:** Five sites (Marsfjäll and north) have calculated no-trap windows ranging from 38 to 74 days. Methodology documented in `ljusberakningar.md`. Uncertainty noted: the two calibration dates (May 31 / Aug 1) give slightly different thresholds; the conservative value (May 31) is used.

## Habitat documentation protocol

**2026-07 — LUCAS-adapted six-photo protocol, campaign in August**
- **What:** Each trap position is documented with six standardised photos (trap view, canopy, N/E/S/W) using the LUCAS land-cover survey methodology. Phone held in landscape mode, ~1/6 sky. One-time campaign in August 2026.
- **Why:** Enables systematic comparison of habitat context across sites and years, consistent with EU-wide survey standards. Coordinates captured automatically via app registration.
- **Impact:** Illustrated in site-specifikationer.md with three illustrations (fallplatser-oversikt.png, habitatdok-ovanifraan.png, habitatdok-foton.png).

## Video and media decisions

**2026-07 — YouTube Shorts used for portrait screen recordings**
- **What:** App walkthrough screen recordings (registration, editing observations) are uploaded as YouTube Shorts and embedded using `.video-wrapper-portrait` (280×498px fixed dimensions, 9:16 aspect ratio).
- **Why:** Shorts are naturally portrait format; the fixed-dimension wrapper avoids the percentage-padding approach which doesn't work cleanly with constrained widths.
- **Impact:** Separate CSS class from the landscape `.video-wrapper` used for assembly videos.

**2026-07 — Watercolor illustrations generated in ChatGPT from Lars's sketches and instructions**
- **What:** The site deployment overview (fallplatser-oversikt.png), overhead documentation illustration (habitatdok-ovanifraan.png), and trap watercolor illustrations were generated using ChatGPT image generation following Lars's detailed prompts and sketches.
- **Why:** Produces a consistent visual style that complements the existing watercolor trap illustration. No external attribution required.
- **Impact:** Images are effectively Lars's own work; treated the same as other project-produced assets.

## Contributor attribution and AI disclaimer

**2026-07-26 — om-manualen.md page created**
- **What:** A dedicated page listing contributors, funding, project partners, and an AI
  disclaimer. Credit line for contributors added visibly on index.md, not buried in footer.
- **Why:** The manual may become a citable product (DOI pending). Contributors need proper
  attribution. The AI disclaimer follows emerging best practice for research outputs.
- **Impact:** "Framtagen av" used instead of "Ansvarig utgivare" (a specific Swedish press
  law term that doesn't apply here).

## Feedback and issue tracking

**2026-07-26 — Google Form + Sheets over GitHub Issues**
- **What:** Participant feedback collected via Google Form → private Google Sheet. A public
  view (Publik vy tab) is embedded in synpunkter.md showing status of all items.
- **Why:** GitHub Issues require an account, English, and are visible to the entire European
  ABLE user base — too high a barrier for citizen scientist participants. Google Form is
  zero-friction. The embedded public view gives transparency without GitHub overhead.
- **Impact:** rapportera-tekniskt-fel.md still gates true technical bugs (ask Lars first,
  then file on GitHub if genuinely new). The form handles everything else.
- **Status values:** Ny, Under behandling, Åtgärdad, Vidarebefordrad, Noterat ingen åtgärd
  ("Noterat ingen åtgärd" chosen over "Ej relevant" — softer, less dismissive)

## Rutnät position maps removed from public manual

**2026-07-26 — Exact trap positions withheld pending collaborator discussion**
- **What:** Numbered position maps for Silvåkra, Björnstorp, Uppsala A/B removed from
  rutnat-lund-uppsala.md. Replaced with a note pointing to separate participant documents.
- **Why:** The manual is public. Precise GPS positions of research sites carry a small but
  real risk of disturbance by the public or competing collectors. Decision made conservatively
  pending discussion with collaborators (Anders Björkén, SLU).
- **Impact:** Maps still exist as image assets in docs/assets/images/rutnat/ and can be
  reinstated. The two people actually running the grid already know the positions.
- **Resolution (2026-07-27)**: rather than withhold the maps indefinitely, a displacement approach was developed and shipped instead (see entry below) — maps are back in the public manual, but show deliberately shifted, non-real positions.

## Darkness window reframe

**2026-07-26 — ljusberakningar.md rewritten as "standardising disturbing background light"**
- **What:** The page originally framed the topic as "ljusuppehåll" (trap pauses). Rewritten
  to frame it as: what threshold of background light makes light traps unsatisfactory, and
  when can reliable sampling resume?
- **Why:** Lars's preferred scientific framing — the threshold definition is the
  contribution, not the dates. Also more honest: participants are invited to try earlier than
  the calculated dates, and observations near the boundaries are valuable for calibration.
- **Impact:** Column headers in the results table now read "Bakgrundsljuset stör från /
  Provtagning kan återupptas" rather than "Fällorna stängs / öppnar igen".

## Project contact email

**2026-07-28 — LU list alias switchover deferred to mid-August**
- **What:** The nattfjarilar@biol.lu.se list alias is now set up, but the manual and contact pages continue using nattflyn@gmail.com for the time being. Actual switchover targeted for mid-August.
- **Why:** Participants are mid-season and actively using the current address; changing it now risks confusion and missed messages. Deferring to mid-August avoids disrupting an established channel during active fieldwork.
- **Impact:** kontakt-och-stod/whatsapp-och-kontakt.md, rapportera-tekniskt-fel.md, and other pages referencing nattflyn@gmail.com stay as-is until the mid-August switch; CHANGELOG.md backlog item remains open until then.

## Rutnät position maps — displacement approach RESOLVED

**2026-07-27 — Displaced maps successfully completed (v0.9.0)**
- **What:** All four displaced maps (Skåne A/B, Uppland A/B) are finished and live in rutnat-lund-uppsala.md, using real basemap exports and rigidly-shifted positions.
- **Why the earlier attempts failed:** The first round of QGIS exports were wide, low-resolution tiles (5.4-6.1m/px) that couldn't reproduce the original basemap's sharpness — cropping to the required geographic coverage meant heavy upscaling and pixelation. Coordinate-system confusion also caused marker misplacement in a couple of early attempts.
- **What actually fixed it:**
  1. Lars re-exported from QGIS centered directly on each site's *displaced* coordinates (not the real ones) at proper resolution, using the Lantmäteriet Topografiska Webbkartan basemap.
  2. Rather than trust QGIS's own scale bar decoration (which showed the wrong measurement), Claude detects the visible 1×1km reference square directly in each exported image via image analysis — finds long unbroken dark line-runs (distinguishing the square's border from text, which breaks into short segments) — giving an exact pixel-to-meter calibration per image with no coordinates or projection involved. All four images calibrated identically (~2057px = 1000m), confirming the QGIS exports were consistent. The 250m scale bar is drawn directly from that measurement.
  3. For Uppland A/B specifically (no real GPS trap positions, only the official 1km survey squares), the 3×3 grid is generated fresh via bilinear interpolation directly from each square's own four corners (entirely within SWEREF99TM/EPSG:3006, no lat/lon conversion) rather than a separately-displaced point layer — this guarantees the grid and the square can never misalign, since the points are mathematically derived from the square itself.
- **Impact:** Real GPS confirmed and used for Skåne A/B. Uppland A/B use the square-derived grid (not real registered trap positions — still on the backlog, see Unreleased in CHANGELOG.md). Original real-position images kept for Lars's own bookkeeping in `docs/assets/images/precise-maps/`, gitignored, never pushed publicly. Displacement amounts unchanged from below.
- **Displacement amounts:** Skåne A: 1km W + 500m S; Skåne B/Uppland B: 1km E + 500m S;
  Uppland A: 2km E + 500m S.
  
  ## PDF export

**2026-07-28 — Manual local build script over CI automation**
- **What:** PDF export is a local script (`build_pdf.py`, Playwright + pypdf) run
  manually whenever an updated PDF is wanted, not a GitHub Actions workflow
  triggered on push.
- **Why:** Consistent with the project's existing "keep infrastructure
  proportional to a ~15-person audience" stance (see Manual format and platform,
  Feedback and issue tracking above). A CI-automated rebuild would keep the PDF
  perfectly in sync but adds a standing pipeline dependency (secrets, runner
  updates, silent failure risk) for a document that only needs occasional
  refreshing.
- **Impact:** The PDF can lag behind the live site between manual runs. Rerun
  the script and commit after any meaningful content change.

**2026-07-28 — PDF filename is not versioned**
- **What:** Output is always `docs/assets/pdf/nattfjarilar-manual.pdf`, not
  `nattfjarilar-manual-v0.9.1.pdf`-style.
- **Why:** A versioned filename would need the download link on index.md and
  alla-sidor.md updated in lockstep with every version bump — an easy step to
  forget, resulting in a dead link (404) until caught. A stable filename means
  the PDF is simply overwritten in place; git history still preserves every
  prior version if needed.
- **Impact:** The PDF's own generated cover page (title, version, date) is the
  only place version information appears on the document itself.
