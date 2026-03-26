#!/usr/bin/env python3
"""
Converte un file PDF in Markdown.
Uso: python3 pdf_to_md.py file.pdf [output.md]
"""

import sys
import re
from pathlib import Path
import fitz  # pymupdf


def pdf_to_markdown(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)
    title = pdf_path.stem.replace("-", " ").replace("_", " ")
    lines = [f"# {title}", ""]

    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        page_lines = []

        for block in blocks:
            if block["type"] != 0:  # 0 = testo
                continue
            for line in block["lines"]:
                text = " ".join(span["text"] for span in line["spans"]).strip()
                if not text:
                    continue

                # Determina se è un titolo basandosi sulla dimensione font
                max_size = max(span["size"] for span in line["spans"])
                is_bold  = any(span["flags"] & 2**4 for span in line["spans"])

                if max_size >= 14 or (max_size >= 12 and is_bold):
                    page_lines.append(f"\n## {text}")
                elif max_size >= 11 and is_bold:
                    page_lines.append(f"\n### {text}")
                else:
                    page_lines.append(text)

        if page_lines:
            lines.append(f"<!-- Pagina {page_num} -->")
            lines.extend(page_lines)
            lines.append("")

    doc.close()
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 pdf_to_md.py file.pdf [output.md]")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"File non trovato: {pdf_path}")
        sys.exit(1)

    md_content = pdf_to_markdown(pdf_path)

    out_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else pdf_path.with_suffix(".md")
    out_path.write_text(md_content, encoding="utf-8")
    print(f"Creato: {out_path} ({len(md_content):,} caratteri)")
