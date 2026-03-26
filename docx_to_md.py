#!/usr/bin/env python3
"""
Converte un file Word (.docx) in Markdown.
Uso: python3 docx_to_md.py file.docx [output.md]
"""

import sys
from pathlib import Path
from docx import Document
from docx.shared import Pt


# Mapping stili Word → livello heading Markdown
HEADING_STYLES = {
    "heading 1": "#",
    "heading 2": "##",
    "heading 3": "###",
    "heading 4": "####",
    "titolo 1": "#",
    "titolo 2": "##",
    "titolo 3": "###",
}


def para_to_md(para) -> str | None:
    """Converte un paragrafo Word in una riga Markdown."""
    text = para.text.strip()
    if not text:
        return None

    style = para.style.name.lower()

    # Heading
    for key, prefix in HEADING_STYLES.items():
        if style.startswith(key):
            return f"{prefix} {text}"

    # Lista puntata
    if style.startswith("list") or para.style.name.startswith("List"):
        level = para._p.pPr.numPr.ilvl.val if (
            para._p.pPr is not None and
            para._p.pPr.numPr is not None and
            para._p.pPr.numPr.ilvl is not None
        ) else 0
        indent = "  " * level
        return f"{indent}- {text}"

    # Testo normale (grassetto come heading se è breve)
    is_bold = all(run.bold for run in para.runs if run.text.strip())
    if is_bold and len(text) < 100:
        return f"### {text}"

    return text


def docx_to_markdown(docx_path: Path) -> str:
    doc = Document(docx_path)
    title = docx_path.stem.replace("-", " ").replace("_", " ")
    lines = [f"# {title}", ""]

    for para in doc.paragraphs:
        try:
            md_line = para_to_md(para)
        except Exception:
            md_line = para.text.strip() or None

        if md_line:
            lines.append(md_line)

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 docx_to_md.py file.docx [output.md]")
        sys.exit(1)

    docx_path = Path(sys.argv[1])
    if not docx_path.exists():
        print(f"File non trovato: {docx_path}")
        sys.exit(1)

    md_content = docx_to_markdown(docx_path)

    out_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else docx_path.with_suffix(".md")
    out_path.write_text(md_content, encoding="utf-8")
    print(f"Creato: {out_path} ({len(md_content):,} caratteri)")
