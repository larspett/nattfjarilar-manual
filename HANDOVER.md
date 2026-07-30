# Handover — Pilotprojekt nattfjärilar 2026 manual

Read this first in any new session. It is the single source of truth for continuity.
Detailed record lives in DECISIONS.md and CHANGELOG.md at the repo root.

**Before doing any full-repo file handoff**: this project has been worked on by more than
one Claude session/tool directly on Lars's repo. A local working copy in one chat session
can easily be stale relative to what's actually in the repo. Ask Lars to confirm his repo's
current state (or paste his current CHANGELOG.md/DECISIONS.md) before assuming your copy is
current, and prefer sharing only the specific files you've actually changed over a full-repo
zip unless Lars explicitly confirms a full resync is safe. Also note: **DECISIONS.md and
CHANGELOG.md can themselves drift out of sync with each other** if updated by different
sessions at different times — always check both files' dates against each other rather than
trusting either blindly.

---

## NEW FOCUS (2026-07-30): methods paper for Approaches in Entomology

If this new session's purpose is the **publication effort** rather than manual
maintenance, start here instead of the manual-status sections below.

**Prime target: Approaches in Entomology** (Wiley/Royal Entomological Society,
brand-new 2025 journal, scope = methods/techniques/philosophy in entomology —
a strong fit for this project's standardised workflow). **Plan: post a preprint
to EcoEvoRxiv first, then submit to the journal citing the preprint.** Lars
targeted initiation as early as the week of 2026-08-03.

Full rationale, cost confirmation (Bibsam covers the APC at zero cost via Lund
University — no waiver/discount needed), the two other candidates considered
(Biodiversity Data Journal, RIO Journal — also Bibsam-covered), and practical
next steps (draft via the same dialogue approach used for the ADMIRE Moths
application, confirm co-authorship with Harriet Arnberg/Amanda Ernstsson/Ana
Teodora Ştefan, EcoEvoRxiv deposit, then AIE submission) are all in
**DECISIONS.md, under "Methods paper (prime target set 2026-07-30...)"**.

---

## What this project is

A field manual for a 2026 Swedish moth monitoring pilot, hosted as a public Jekyll/GitHub
Pages website at https://larspett.github.io/nattfjarilar-manual/, **now fully bilingual
(Swedish + English)**. ~15 participants run light traps at sites across Sweden (grid
sub-project in Lund/Uppsala; 15-site Lund-to-Abisko latitude gradient).
Current version: **v0.11.0 (2026-07-29)**.

Lars B. Pettersson (lars.pettersson@biol.lu.se), Biologiska institutionen, Lunds
universitet. Contributors: Harriet Arnberg, Amanda Ernstsson, Ana Teodora Ştefan (all LU).
Funded by Naturvårdsverket, contract NV-26-076242.

---

## Site status: essentially complete, bilingual, with PDF export

All Swedish pages have real content (proofread 2026-07-26) and now have a matching
English translation under `/en/`, mirroring the structure 1:1. A downloadable PDF exists
for both languages. A language toggle sits in the site header on every page.

Repo: github.com/larspett/nattfjarilar-manual (public)

**Page inventory** (Swedish paths shown; each has an identical English counterpart under
`en/<same path>`):
```
index.md, om-manualen.md, alla-sidor.md
bakgrund/bakgrund.md
falltyper/oversikt.md
hur-du-satter-ut/site-specifikationer.md, gradient-lund-abisko.md,
  ljusberakningar.md, rutnat-lund-uppsala.md, qr-koder-utrustning.md
under-experimentet/vecko-rutin.md
hur-du-rapporterar/registrera-falla.md, app-instrux.md,
  vad-som-raknas.md, andra-observationer.md
efter-inrapportering/validering.md, forvantade-resultat.md
kontakt-och-stod/whatsapp-och-kontakt.md, rapportera-tekniskt-fel.md,
  nyheter.md, synpunkter.md
```
(`qr-koder-utrustning.md` is new as of v0.11.0-era work — see "Hardware labelling /
QR codes" below.)

**Infrastructure:**
- Jekyll/Cayman, GitHub Pages from /docs on main
- Version: `{{ site.version }}` / `{{ site.version_date }}` in docs/_config.yml
- CSS: docs/assets/css/style.scss — palette #C88030/#63533F/#F6EADA
- CSS classes: `.video-wrapper` (16:9), `.video-wrapper-portrait` (9:16 280×498px),
  `.app-screenshot` (max 260px), `.app-figure`/figcaption, `.print-video-link`
  (print-only clickable video fallback — see PDF export section below)
- DO NOT use where_exp/group_by in Liquid — breaks GitHub Pages' old Liquid parser
- `/en/` folder mirrors `docs/` 1:1 for the English translation. Language toggle in
  `docs/_layouts/default.html` header (Liquid conditional on whether `page.url` contains
  `/en/`). Linking rule for any new page: links between two already-translated pages use
  the exact same relative path as the Swedish original; links to a NOT-yet-translated
  page (or any image/asset, which are never duplicated into `en/`) need exactly one extra
  `../` compared to the Swedish original, per folder-depth. Full details in DECISIONS.md
  under "English translation".
- `build_pdf.py` (repo root, run manually via `conda activate pdfexport`) generates BOTH
  `docs/assets/pdf/nattfjarilar-manual.pdf` (Swedish) and `nattfjarilar-manual-en.pdf`
  (English) in one run. Not versioned filenames — links never go stale on a version bump.

---

## RESOLVED (older items, brief — full writeups in DECISIONS.md)

- **Rutnät position maps** (v0.9.0): displaced/anonymized maps live for all 4 sites.
  Uppland A/B still use a square-derived grid, not real GPS (see Open items below).
- **YouTube video loading failures** (v0.9.1): re-uploaded with proper caption tracks,
  fixed slow/failing iframes.
- **English translation** (v0.11.0): all 19 pages translated, `/en/` mirror live,
  language toggle working.
- **PDF export, both languages** (v0.10.0 → v0.11.0): `build_pdf.py` builds both editions.
- **QR-koder till utrustningen page**: new page covering the hardware-labelling QR-code
  stickers (already physically made and in place on the traps/modules/powerbanks, not
  yet distributed to participants or reflected in the database). Linked from index.md
  and cross-referenced from site-specifikationer.md's August campaign section.
- **PDF export bug batch** (2026-07-30, both languages): cover-page email wasn't a real
  mailto link (fixed); cover illustration printed with a grey halo — actually the live
  site's `box-shadow` printing through, stripped in print CSS; video fallback text was
  never clickable (CSS `::after` content can never be a real link — fundamental
  limitation) — fixed by adding a real hidden `<a class="print-video-link">` inside every
  video-wrapper div, shown only in print with the iframe hidden instead; some pages
  (e.g. LUCAS Atlas) showed duplicate URLs because the print CSS appended `(url)` after
  every link including image-wrapped ones — fixed by excluding `a[href]:has(img)`;
  English PDF cover hardcoded the Swedish project name as its title — now reads
  "Moth Pilot Project 2026".
- **cc_lang_pref video captions**: attempting to force SV/EN captions via the
  `cc_lang_pref` URL parameter proved unreliable (YouTube remembers a viewer's own
  last-selected caption language per account/browser, overriding the URL hint) — decision
  made to stop fighting this; both language pages embed the same dual-caption video and
  let viewers pick manually via the CC button.
- **English feedback form**: after some add-on friction, a working English Google Form
  is live at https://forms.gle/AwpVWosEwWKSpiD4A, linked from the two English contact
  pages (separate from the Swedish form's tracking sheet — English submissions arrive by
  email only, no visible status tracker).
- **kärnlokaler→huvudlokaler, mailto consistency, referrerpolicy on all videos**: all
  resolved, no longer open items.

---

## Open items — as of 2026-07-30

### Still genuinely open
- **Uppland A/B actual GPS trap positions**: still not registered/provided — manual
  shows the square-derived grid, not real positions. Once Lars provides real GPS, redo
  those two maps the same way Skåne A/B were done (displacement offsets: Uppland A 2km E
  + 500m S; Uppland B 1km E + 500m S). No longer top priority, just pending.
- **validering.md**: step-by-step guide still pending a website UI feature (project
  filtering) not yet available.
- **Arnberg & Pettersson 2026**: add link in app-instrux.md once the doc is live on LU
  Research Portal.
- **Nets for trap emptying**: note in vecko-rutin.md once they actually arrive.
- **August habitat documentation campaign**: confirm exact dates once set.
- **QR-koder page**: still needs photos of the smaller light-module stickers (once
  received) and a short instructional video showing exact placement on each device type.
- **References and Acknowledgements sections**: not yet added.
- **Project email LU list alias** (nattfjarilar@biol.lu.se): the list itself is set up
  and ready, but Lars is deliberately deferring the actual switchover to mid-August to
  avoid mid-season confusion — this is scheduled, not forgotten.
- **DOI**: superseded by the methods-paper plan above — no longer a standalone "get a
  bare DOI" task, folded into the paper's eventual publication.

---

## YouTube videos (current, confirmed correct 2026-07-29)

Assembly (16:9, `.video-wrapper`) — **same real video ID used on both language pages**,
each video already contains both SV+EN caption tracks (viewer selects via CC button):
- LED-Emmer: 5JjvBHtwObg
- LED-Emmer Quad: KGVXMc3BJPg
- LED-Emmer Quad funnel: Tq-d2nS3o_Q
- EntoLight (Twincolor & Multicolor): QI6Ho9qigdY
- Powerbank troubleshooting: qp0osTlcAnk
- Channel: @dagfjarilar

(A separate "EN video ID" list existed briefly in this project's history and turned out
to be entirely fabricated/non-existent IDs — confirmed by Lars, fixed 2026-07-29. Don't
trust a "parallel EN video ID list" without confirming it against the actual YouTube
channel first.)

Screen recording Shorts (9:16, `.video-wrapper-portrait`) — no separate EN version, same
ID both languages (silent screen recordings):
- Registrera lokal: VuQDXFuceyQ
- Se och ändra observationer: HNRSdiz2gkQ
- Ändra antal: jnCcrTTZ6Nk

Swedish feedback form: https://forms.gle/5Vrf68vXGjDm9eEv9 (Public embed in synpunkter.md:
Google Sheets Publik vy tab, gid=502981035)
English feedback form: https://forms.gle/AwpVWosEwWKSpiD4A (email-only, no tracker)

---

## Lars's working preferences

- Avoids em dashes (AI detection signal), Microsoft tools
- Prefers minimal-intervention edits with clear reasoning
- Terminology: ljusmodul, vingar, tömning av fällan (not vittjning); "sätta ut" → "put
  out"/"putting out" for concrete everyday actions, "deploy"/"deploying" for the more
  abstract/methodological framing (e.g. page titles about general principles)
- Palette: cream #F6EADA, brown #63533F, accent #C88030
- Primary Swedish regulatory sources over secondary
- Wants ready-to-paste git commands (add/commit/push) alongside any file handoff — but
  skip `cd`/`cp` boilerplate, he already works directly in the repo directory
