#!/usr/bin/env python3
"""
build_pdf.py — Pilotprojekt nattfjärilar 2026 manual: PDF export

Renders every page of the live manual (https://larspett.github.io/nattfjarilar-manual/)
to PDF via a headless browser (print stylesheet applies automatically), then merges
everything into a single versioned PDF under docs/assets/pdf/.

Run this manually whenever you want to refresh the downloadable PDF (e.g. after a
version bump). It is NOT wired into any CI — nothing runs unless you run it.

Usage:
    pip install playwright pypdf --break-system-packages
    playwright install chromium
    python3 build_pdf.py

Requires: Python 3.9+, Playwright with Chromium installed (see above).
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfWriter

# ---------------------------------------------------------------------------
# Configuration — edit these if the site structure changes
# ---------------------------------------------------------------------------

BASE_URL = "https://larspett.github.io/nattfjarilar-manual"

# Page order matches the manual's actual reading order (per HANDOVER.md page
# inventory), NOT alphabetical. Update this list if pages are added/removed/renamed.
SV_PAGES = [
    "",  # index.md
    "/om-manualen",
    "/bakgrund/bakgrund",
    "/falltyper/oversikt",
    "/hur-du-satter-ut/site-specifikationer",
    "/hur-du-satter-ut/gradient-lund-abisko",
    "/hur-du-satter-ut/ljusberakningar",
    "/hur-du-satter-ut/rutnat-lund-uppsala",
    "/under-experimentet/vecko-rutin",
    "/hur-du-rapporterar/registrera-falla",
    "/hur-du-rapporterar/app-instrux",
    "/hur-du-rapporterar/vad-som-raknas",
    "/hur-du-rapporterar/andra-observationer",
    "/efter-inrapportering/validering",
    "/efter-inrapportering/forvantade-resultat",
    "/kontakt-och-stod/whatsapp-och-kontakt",
    "/kontakt-och-stod/rapportera-tekniskt-fel",
    "/kontakt-och-stod/nyheter",
    "/kontakt-och-stod/synpunkter",
]

# Same reading order, same pages, just under /en/. Keep this list in lockstep
# with SV_PAGES above — if a Swedish page is added/removed/renamed, mirror the
# change here once the English translation exists.
EN_PAGES = ["/en" + p if p else "/en" for p in SV_PAGES]

OUTPUT_DIR = Path("docs/assets/pdf")

# Update MANUAL_VERSION/MANUAL_VERSION_DATE by hand when the version bumps —
# these appear on the generated cover page only. Output filenames are
# intentionally NOT versioned so the download links on index.md/alla-sidor.md
# (both languages) never go stale on a version bump.
MANUAL_VERSION = "0.10.0"
MANUAL_VERSION_DATE = "2026-07-28"
TMP_DIR = Path(".pdf_build_tmp")


def cover_html(title: str, subtitle: str, author_block: str) -> str:
    """Generate the cover page HTML for one language edition."""
    return f"""
<html>
<head>
<style>
  body {{
    font-family: 'Helvetica Neue', Arial, sans-serif;
    margin: 0;
    padding: 0;
    background: #FFFDF9;
  }}
  .cover {{
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 0 10%;
  }}
  h1 {{
    color: #C88030;
    font-size: 2.4em;
    margin-bottom: 0.2em;
  }}
  h2 {{
    color: #63533F;
    font-weight: normal;
    font-size: 1.3em;
    margin-top: 0;
  }}
  .meta {{
    margin-top: 3em;
    color: #63533F;
    font-size: 1em;
    line-height: 1.6;
  }}
</style>
</head>
<body>
  <div class="cover">
    <h1>{title}</h1>
    <h2>{subtitle}</h2>
    <div class="meta">
      {author_block}<br>
      lars.pettersson@biol.lu.se<br>
      <br>
      Version {MANUAL_VERSION} &middot; {MANUAL_VERSION_DATE}
    </div>
  </div>
</body>
</html>
"""


# One entry per language edition. Add/edit here if the site gets a third
# language, or if either edition's cover text/page list needs a tweak.
EDITIONS = [
    {
        "name": "Swedish",
        "pages": SV_PAGES,
        "output_filename": "nattfjarilar-manual.pdf",
        "cover_html": cover_html(
            "Pilotprojekt nattfjärilar 2026",
            "Fältmanual",
            "Lars B. Pettersson<br>Biologiska institutionen, Lunds universitet",
        ),
    },
    {
        "name": "English",
        "pages": EN_PAGES,
        "output_filename": "nattfjarilar-manual-en.pdf",
        "cover_html": cover_html(
            "Pilotprojekt nattfjärilar 2026",
            "Field manual",
            "Lars B. Pettersson<br>Department of Biology, Lund University",
        ),
    },
]


def render_cover_page(html: str, tmp_dir: Path) -> Path:
    """Render a given cover page HTML string to its own PDF."""
    cover_html_path = tmp_dir / "cover.html"
    tmp_dir.mkdir(exist_ok=True)
    cover_html_path.write_text(html, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file://" + str(cover_html_path.resolve()))
        out_path = tmp_dir / "page_cover.pdf"
        page.pdf(path=str(out_path), format="A4", print_background=True)
        browser.close()

    return out_path


def render_pages(base_url: str, pages: list[str], tmp_dir: Path) -> list[Path]:
    """Render each page URL to its own PDF file via headless Chromium, print media."""
    tmp_dir.mkdir(exist_ok=True)
    pdf_paths = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.emulate_media(media="print")

        for i, path in enumerate(pages):
            url = base_url.rstrip("/") + "/" + path.lstrip("/")
            print(f"[{i + 1}/{len(pages)}] Rendering {url}")
            page.goto(url, wait_until="networkidle", timeout=30_000)

            # Give embedded iframes / lazy content a moment to settle. This does not
            # wait for video playback (videos are hidden entirely in print CSS —
            # see the .no-print / print-fallback rules in style.scss).
            page.wait_for_timeout(500)

            out_path = tmp_dir / f"page_{i:02d}.pdf"
            page.pdf(
                path=str(out_path),
                format="A4",
                print_background=True,
                margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            )
            pdf_paths.append(out_path)

        browser.close()

    return pdf_paths


def merge_pdfs(pdf_paths: list[Path], output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    for pdf_path in pdf_paths:
        writer.append(str(pdf_path))
    with open(output_file, "wb") as f:
        writer.write(f)
    writer.close()


def cleanup(tmp_dir: Path) -> None:
    for f in tmp_dir.iterdir():
        f.unlink()
    tmp_dir.rmdir()


def build_edition(edition: dict) -> Path:
    """Build one language edition's PDF and return its output path."""
    output_file = OUTPUT_DIR / edition["output_filename"]
    print(f"--- Building {edition['name']} edition ---")

    cover_path = render_cover_page(edition["cover_html"], TMP_DIR)
    pdf_paths = [cover_path] + render_pages(BASE_URL, edition["pages"], TMP_DIR)
    print(f"Merging {len(pdf_paths)} pages into {output_file} ...")
    merge_pdfs(pdf_paths, output_file)
    cleanup(TMP_DIR)

    print(f"Done: {output_file}")
    return output_file


def main() -> int:
    if not (Path("docs") / "_config.yml").exists():
        print(
            "Warning: docs/_config.yml not found in the current directory.\n"
            "Run this script from the repo root (nattfjarilar-manual/).",
            file=sys.stderr,
        )

    output_files = [build_edition(edition) for edition in EDITIONS]

    print("\nAll editions built:")
    for f in output_files:
        print(f"  {f}")
    print(f"Remember to git add/commit/push {', '.join(str(f) for f in output_files)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
