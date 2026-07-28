#!/usr/bin/env python3
"""
build_pdf.py — Pilotprojekt nattfjärilar 2026 manual: PDF export

Renders every page of the live manual (https://larspett.github.io/nattfjarilar-manual/)
to PDF via a headless browser (print stylesheet applies automatically), then merges
everything into a single docs/assets/pdf/manual.pdf.

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
PAGES = [
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

OUTPUT_DIR = Path("docs/assets/pdf")
OUTPUT_FILE = OUTPUT_DIR / "manual.pdf"
TMP_DIR = Path(".pdf_build_tmp")

# ---------------------------------------------------------------------------


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
    for f in tmp_dir.glob("*.pdf"):
        f.unlink()
    tmp_dir.rmdir()


def main() -> int:
    if not (Path("docs") / "_config.yml").exists():
        print(
            "Warning: docs/_config.yml not found in the current directory.\n"
            "Run this script from the repo root (nattfjarilar-manual/).",
            file=sys.stderr,
        )

    pdf_paths = render_pages(BASE_URL, PAGES, TMP_DIR)
    print(f"Merging {len(pdf_paths)} pages into {OUTPUT_FILE} ...")
    merge_pdfs(pdf_paths, OUTPUT_FILE)
    cleanup(TMP_DIR)

    print(f"Done: {OUTPUT_FILE}")
    print("Remember to git add/commit/push docs/assets/pdf/manual.pdf.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
