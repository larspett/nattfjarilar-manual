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

**2026 — No standalone FAQ; "När det krånglar" + "senaste lärdomarna" instead**
- **What:** Troubleshooting content lives as a running, dated list tied to the Nyheter/changelog page, not a separate static FAQ.
- **Why:** Static FAQs get less attention over time; a page that's visibly "alive" (tied to update history) holds attention better for a small, engaged group.

## Project design and deployment rules

**2026 — Trap type is randomly assigned per site and fixed for the season**
- **What:** At each gradient site, 4 trap locations are chosen ≥50m apart, then trap type is assigned to each location by drawing lots. That assignment is fixed for the whole season; participants may experiment with trap placement outside official weekly trials, but not during them.
- **Why:** Protects the experimental design (site×trap-type confounding) against well-intentioned participant "improvements" mid-season.
- **Impact:** Needs strong, close-to-sign-off-level communication in the manual, since the failure mode is a well-meaning participant changing something.

**2026 — Artportalen sync framed as a goal, not a promise**
- **What:** Manual tells participants the concrete, deliverable fact (data can always be exported and manually imported to Artportalen) and frames automatic sync as a future aim, not a current feature.
- **Why:** Automatic sync requires both participant consent and Artdatabanken's approval, which hasn't been granted. Overpromising a feature that depends on a third party's cooperation risks a manual that ages badly.

**2026 — Participant contact/address list kept out of the manual entirely**
- **What:** A separate, participant-only document handles names/addresses/contact sharing consent; the manual itself never includes this.
- **Why:** Keeps the manual shareable/public-facing without a privacy dependency, and keeps the consent scope for that separate document clean and specific.

## Cover illustration

**2026-07 — Sweden outline sourced from real boundary data, not hand-drawn**
- **What:** Switched from a ~50-point freehand approximation to the actual Natural Earth boundary (3,388-point mainland + real islands) via the public `datasets/geo-countries` GitHub dataset.
- **Why:** The hand-drawn version read as an unrecognizable blob; this was misdiagnosed for a while as a projection/tiling problem before the real cause (bad source geometry) was found.
- **Impact:** Both the gradient map and grid-insets map use this same boundary data.

**2026-07 — Grid-insets map uses real OpenFreeMap basemap images, not blank/illustrative panels**
- **What:** Each of the four grid insets (Skåne 45/96, Uppland A/B) shows an actual cropped OpenFreeMap Bright export as its background, precisely georeferenced and cropped via world-file (.jgw) math.
- **Why:** A long back-and-forth (line weight, dot size, background wash, deeper land fill) tried to fix a "the grid-insets map looks too pale/thin next to the other illustrations" problem by styling alone. None of it worked structurally. Real map tiles carry genuine visual density that styling tweaks on a blank background can't replicate.
- **Impact:** This was the fix that actually worked; resolved a long-running back-and-forth. Front cover uses this version (grid_insets_cover_v7.jpg) as final.

**2026-07 — Front cover is 4 independently-produced pieces assembled by Lars, not one Claude-built composite**
- **What:** Moth icon, gradient map, grid-insets map, and trap-illustration are each finished separately; Lars assembles and exports the final joined composite himself from his own layout tool.
- **Why:** A first assembly attempt (reverse-engineering proportions from a screenshot) was necessarily approximate; exporting from the source layout tool that already has the exact allocation is more reliable than reconstructing it.

## Manual hosting (supersedes earlier "no GitHub" call)

**2026-07 — Manual is hosted on GitHub Pages, repo also serves as project bookkeeping**
- **What:** The GitHub repo hosts the manual's markdown source (in `/docs`) and is also where DECISIONS.md and CHANGELOG.md live for project record-keeping. GitHub Pages is configured to serve directly from `main` branch, `/docs` folder — no separate build branch, no local tooling.
- **Why:** Earlier decision ("Manual format and platform" above) rejected GitHub/MkDocs as infrastructure the ~15-person audience didn't need. That still holds for the *editing* workflow, but GitHub Pages' built-in Jekyll processing (zero local setup, auto-builds on push) turns out to be a low-effort way to satisfy the original requirement (versioned website with section-jumping) without contradicting the earlier "keep it simple" reasoning.
- **Impact:** Existing `/docs` skeleton can be used as-is. Each markdown file needs minimal Jekyll front matter to be processed. Relative `.md` links between pages work automatically via GitHub Pages' built-in `jekyll-relative-links` plugin — no need to rewrite links to `.html`.

