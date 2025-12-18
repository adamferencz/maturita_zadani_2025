#!/usr/bin/env python3
"""
Skript pro konverzi Markdown souborů na PDF pomocí pypandoc
"""
import os
import sys
from pathlib import Path
import pypandoc

def convert_md_to_pdf(md_file_path):
    """Převede Markdown soubor na PDF"""
    md_path = Path(md_file_path)
    
    if not md_path.exists():
        print(f"Soubor {md_file_path} neexistuje!")
        return False
    
    # Určení výstupní cesty
    output_path = md_path.with_suffix('.pdf')
    
    try:
        # Konverze pomocí pypandoc
        # Pokud pandoc nenalezne pdf engine, konvertuje na HTML a to se dá vytisknout z prohlížeče
        pypandoc.convert_file(
            str(md_path),
            'pdf',
            outputfile=str(output_path),
            extra_args=[
                '-V', 'geometry:margin=2.5cm',
                '-V', 'fontsize=11pt',
                '--pdf-engine=wkhtmltopdf'
            ]
        )
        print(f"✓ Úspěšně vytvořeno: {output_path.name}")
        return True
    except Exception as e:
        # Pokud PDF engine není dostupný, vytvoříme HTML
        print(f"⚠ PDF engine není dostupný pro {output_path.name}, vytvářím HTML...")
        try:
            html_output = md_path.with_suffix('.html')
            pypandoc.convert_file(
                str(md_path),
                'html5',
                outputfile=str(html_output),
                extra_args=['-s', '--metadata', 'title=Zadání maturitní práce']
            )
            print(f"✓ Vytvořen HTML soubor: {html_output.name} (otevřete v prohlížeči a vytiskněte jako PDF)")
            return True
        except Exception as e2:
            print(f"✗ Chyba při vytváření {md_path.name}: {str(e2)}")
            return False

def main():
    """Hlavní funkce skriptu"""
    if len(sys.argv) < 2:
        print("Použití: python convert_to_pdf.py <cesta_ke_složce_s_md_soubory>")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    
    if not input_dir.exists() or not input_dir.is_dir():
        print(f"Složka {input_dir} neexistuje!")
        sys.exit(1)
    
    # Najít všechny .md soubory
    md_files = list(input_dir.glob("*.md"))
    
    if not md_files:
        print(f"Ve složce {input_dir} nebyly nalezeny žádné .md soubory!")
        sys.exit(1)
    
    print(f"Nalezeno {len(md_files)} Markdown souborů ke konverzi...\n")
    
    success_count = 0
    for md_file in md_files:
        if convert_md_to_pdf(md_file):
            success_count += 1
    
    print(f"\nHotovo! Úspěšně zpracováno {success_count}/{len(md_files)} souborů.")

if __name__ == "__main__":
    main()
