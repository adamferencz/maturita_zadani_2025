"""Generate PDF versions of posudky from Markdown sources using PyMuPDF Story."""

import fitz
import markdown
import os

POSUDKY_DIR = os.path.join(os.path.dirname(__file__), "odevzdani_2026", "posudky")

MD_FILES = [
    "holecek_posudek_vedouciho.md",
    "holecek_posudek_oponenta.md",
    "jakubek_posudek_vedouciho.md",
    "jakubek_posudek_oponenta.md",
    "joly_posudek_vedouciho.md",
    "joly_posudek_oponenta.md",
    "kotlas_posudek_vedouciho.md",
    "kotlas_posudek_oponenta.md",
    "mikulic_posudek_vedouciho.md",
    "mikulic_posudek_oponenta.md",
]

CSS = """
body {
    font-family: serif;
    font-size: 11pt;
    color: #111;
    line-height: 1.55;
    margin: 0;
    padding: 0;
}
h1 {
    font-size: 15pt;
    font-weight: bold;
    margin-bottom: 6pt;
    padding-bottom: 4pt;
    border-bottom: 1px solid #333;
}
h2 {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 14pt;
    margin-bottom: 4pt;
}
h3 {
    font-size: 11pt;
    font-weight: bold;
    margin-top: 10pt;
    margin-bottom: 3pt;
}
p {
    margin-top: 4pt;
    margin-bottom: 4pt;
}
table {
    border-collapse: collapse;
    margin-bottom: 10pt;
    width: 100%;
}
th, td {
    border: 1px solid #aaa;
    padding: 4pt 8pt;
    font-size: 10pt;
}
th {
    background-color: #eee;
    font-weight: bold;
}
strong {
    font-weight: bold;
}
em {
    font-style: italic;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 10pt 0;
}
ul, ol {
    margin: 4pt 0;
    padding-left: 18pt;
}
li {
    margin-bottom: 2pt;
}
code {
    font-family: monospace;
    font-size: 9pt;
    background: #f4f4f4;
}
"""

MEDIABOX = fitz.paper_rect("A4")
MARGIN = 56
WHERE = fitz.Rect(
    MEDIABOX.x0 + MARGIN,
    MEDIABOX.y0 + MARGIN,
    MEDIABOX.x1 - MARGIN,
    MEDIABOX.y1 - MARGIN,
)


def md_to_pdf(md_path: str, pdf_path: str) -> None:
    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code"],
    )
    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{CSS}</style></head>
<body>{html_body}</body>
</html>"""

    story = fitz.Story(html)
    writer = fitz.DocumentWriter(pdf_path)

    more = 1
    while more:
        device = writer.begin_page(MEDIABOX)
        more, _ = story.place(WHERE)
        story.draw(device)
        writer.end_page()

    writer.close()
    print(f"  OK  {os.path.basename(pdf_path)}")


def main() -> None:
    os.makedirs(POSUDKY_DIR, exist_ok=True)
    print("Generating PDFs...")
    for fname in MD_FILES:
        md_path = os.path.join(POSUDKY_DIR, fname)
        pdf_path = os.path.join(POSUDKY_DIR, fname.replace(".md", ".pdf"))
        if not os.path.exists(md_path):
            print(f"  SKIP {fname} (not found)")
            continue
        md_to_pdf(md_path, pdf_path)
    print("Done.")


if __name__ == "__main__":
    main()
