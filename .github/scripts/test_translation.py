#!/usr/bin/env python3
# .github/scripts/test_translation.py
from pathlib import Path
import sys

def check_translation(src_file, dst_file):
    src_content = src_file.read_text(encoding='utf-8')
    dst_content = dst_file.read_text(encoding='utf-8')
    
    src_lines = [l.strip() for l in src_content.splitlines() if l.strip()]
    dst_lines = [l.strip() for l in dst_content.splitlines() if l.strip()]
    
    print(f"\n=== Comparando {src_file} vs {dst_file} ===")
    print(f"Líneas originales: {len(src_lines)}")
    print(f"Líneas traducidas: {len(dst_lines)}")
    
    # Buscar líginas que no se tradujeron
    untranslated = []
    for i, (src, dst) in enumerate(zip(src_lines[:20], dst_lines[:20]), 1):
        if src == dst and len(src) > 10:  # Si son iguales y tienen contenido
            untranslated.append((i, src[:50] + "..."))
    
    if untranslated:
        print("\nPosibles líneas no traducidas:")
        for line_num, content in untranslated[:5]:
            print(f"  Línea {line_num}: {content}")
    
    return len(untranslated)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: test_translation.py <directorio_original> <directorio_traducido>")
        sys.exit(1)
    
    src_dir = Path(sys.argv[1])
    dst_dir = Path(sys.argv[2])
    
    total_issues = 0
    for src_file in src_dir.rglob("*.adoc"):
        rel_path = src_file.relative_to(src_dir)
        dst_file = dst_dir / rel_path
        
        if dst_file.exists():
            total_issues += check_translation(src_file, dst_file)
    
    print(f"\nTotal de posibles problemas: {total_issues}")