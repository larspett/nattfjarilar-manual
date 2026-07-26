# Handover — Pilotprojekt nattfjärilar 2026 manual

Read this first in any new session. It is the single source of truth for continuity.
The detailed technical record lives in DECISIONS.md and CHANGELOG.md at the repo root.

---

## What this project is

A field manual for a 2026 Swedish moth monitoring pilot, hosted as a public Jekyll/GitHub
Pages website at https://larspett.github.io/nattfjarilar-manual/. About 15 participants
run light traps at sites across Sweden (two sub-projects: a landscape grid in Lund/Uppsala,
and a 15-site Lund-to-Abisko latitude gradient). The manual tells them everything they
need to operate the traps, record catches, and report data.

Lars B. Pettersson (lars.pettersson@biol.lu.se), Biologiska institutionen, Lunds
universitet, is the project lead and sole maintainer of the manual. Manual contributors:
Harriet Arnberg, Amanda Ernstsson, Ana Teodora Ştefan (all LU). Funded by
Naturvårdsverket, contract NV-26-076242.

---

## Current state — v0.7.0 (2026-07-26)

All pages have real content. The proofreading pass is complete. The site is live and
participants have been given the URL.

**Pages in the manual (docs/):**

```
index.md                         — home page, contributor credit, feedback link
om-manualen.md                   — contributors, funding, AI disclaimer
alla-sidor.md                    — auto-generated sitemap (do not edit manually)
bakgrund/
  bakgrund.md                    — EU mandate, project rationale, tools
falltyper/
  oversikt.md                    — all 4 trap models, specs, videos, powerbank tips
hur-du-satter-ut/
  site-specifikationer.md        — trap placement rules, lottery, LUCAS photo protocol
  gradient-lund-abisko.md        — 15 gradient sites, darkness windows
  ljusberakningar.md             — darkness window methodology (depth page)
  rutnat-lund-uppsala.md         — grid sub-project (maps removed pending privacy discussion)
under-experimentet/
  vecko-rutin.md                 — weekly routine, weather, timing, Norrfjärden special case
hur-du-rapporterar/
  registrera-falla.md            — trap registration (web + app walkthrough with Short video)
  app-instrux.md                 — ButterflyCount step-by-step with screenshots
  vad-som-raknas.md              — what counts, species scope, håv/nets note
  andra-observationer.md         — editing observations in app and website (2 Short videos)
efter-inrapportering/
  validering.md                  — validation overview (step-by-step TBD, website UI pending)
  forvantade-resultat.md         — what data will show (placeholder pending real data)
kontakt-och-stod/
  whatsapp-och-kontakt.md        — contact, WhatsApp, feedback form link
  rapportera-tekniskt-fel.md     — technical bug reporting (gated, email Lars first)
  nyheter.md                     — changelog for participants + "när det krånglar" tips
  synpunkter.md                  — embedded Google Sheet showing feedback status
```

**Videos (all on YouTube, embedded in manual):**

Assembly (landscape 16:9, `.video-wrapper`):
- LED-Emmer SV: GrrSlT9ah-M | EN: tYH48SZjwUo
- LED-Emmer Quad SV: hnr4Ww46mHg | EN: 62XC7lHacvI
- LED-Emmer Quad funnel/silicone SV: F8BcoqJBZz4 | EN: OJanLABY1RU
- EntoLight SV: 7UC9A0au6N8 | EN: a891Pv0Imhc
- Powerbank troubleshooting SV: g6WUtUxQUdE | EN: cDKbjC3L4cM

Screen recording Shorts (portrait 9:16, `.video-wrapper-portrait`):
- Registrera lokal: w4kJjqw5moU
- Se och ändra observationer: _5r1490GXuU
- Ändra antal: b2fphWfQHcg

**Feedback system:**
- Form: https://forms.gle/5Vrf68vXGjDm9eEv9
- Public view (embedded in synpunkter.md): Google Sheets Publik vy tab, gid=502981035
- Status dropdown: Ny, Under behandling, Åtgärdad, Vidarebefordrad, Noterat ingen åtgärd

---

## Open items

**Waiting on external actions:**
- Arnberg & Pettersson 2026 link in app-instrux.md → add when correct doc is on LU Research Portal
- Exact August dates for LUCAS habitat documentation campaign → update site-specifikationer.md
- Nets for trap emptying (arriving ~2 weeks from 2026-07-24) → add note to vecko-rutin.md
- Validering.md step-by-step → add in August once website UI (project filtering) is ready
- Live data links → forvantade-resultat.md once pilot data arrives
- Uppsala A/B grid coordinates → rutnat-lund-uppsala.md once real coordinates registered

**Decisions pending:**
- Rutnät position maps: removed from public manual pending discussion with collaborators
  (privacy/disturbance risk). Maps exist in docs/assets/images/rutnat/
- English translation → tomorrow's session
- PDF generation → tomorrow's session

**Terminology (final pass not yet done):**
- kärnlokaler → huvudlokaler (gradient-lund-abisko.md)
- Any remaining vittjning/vittja occurrences
- bakgrund/oversikt links → now bakgrund/bakgrund (index.md updated; check others)

---

## Lars's working preferences

- **File handoff**: Lars works from Box Drive (synced local repo). In chat sessions,
  produce clean files and he downloads/places them. For git, supply exact terminal commands.
- **Terminology**: ljusmodul (not lampa), vingar (support fins), tömning av fällan
  (not vittjning), huvudlokaler (not kärnlokaler)
- **Avoids**: Microsoft tools, em dashes (AI detection signal)
- **Prefers**: minimal-intervention edits with clear reasoning, clean copy-ready text blocks
- **Language**: manual is in Swedish; responses can be in English

---

## Technical details

- Repo: github.com/larspett/nattfjarilar-manual (public)
- Jekyll/Cayman theme, GitHub Pages, serving from /docs on main branch
- Version in docs/_config.yml: `version` and `version_date` variables
- Current version: v0.7.0 (2026-07-26)
- CSS: docs/assets/css/style.scss — palette #C88030 (accent), #63533F (brown), #F6EADA (cream)
- Custom layout: docs/_layouts/default.html — header byline, cover image, top nav
- Liquid: use only basic constructs (for/if/unless/assign) — NO where_exp/group_by,
  they break GitHub Pages' locked older Liquid parser
- Video in git: NEVER — all MP4s gitignored, hosted on YouTube
- CSS classes: `.video-wrapper` (16:9), `.video-wrapper-portrait` (9:16, 280×498px),
  `.app-screenshot` (max-width 260px), `.app-figure` + figcaption styling

---

## Tomorrow's agenda

1. English version of the manual (parallel edition)
2. PDF generation from manual content
