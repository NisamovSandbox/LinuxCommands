#!/usr/bin/env python3
# .github/scripts/test_translation.py
from pathlib import Path
import sys
import re

def count_translatable_lines(content):
    """Cuenta líneas que deberían ser traducidas"""
    lines = content.splitlines()
    count = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Ignorar líneas que no deben traducirse
        if stripped.startswith(('//', ':', '[source', '|===', '----', 'include::')):
            continue
        if re.match(r'^=+\s', stripped):
            continue
        if re.match(r'^\s*[\*\-+]\s*$', stripped):
            continue
        count += 1
    return count

def check_translation(src_file, dst_file):
    src_content = src_file.read_text(encoding='utf-8')
    dst_content = dst_file.read_text(encoding='utf-8')
    
    src_translatable = count_translatable_lines(src_content)
    dst_translatable = count_translatable_lines(dst_content)
    
    print(f"\n=== {src_file.name} ===")
    print(f"Líneas traducibles en original: {src_translatable}")
    print(f"Líneas traducibles en traducción: {dst_translatable}")
    
    # Comparar primeras 10 líneas traducibles
    src_lines = [l.strip() for l in src_content.splitlines() if l.strip()]
    dst_lines = [l.strip() for l in dst_content.splitlines() if l.strip()]
    
    issues = 0
    print("\nMuestra de comparación:")
    
    for i in range(min(20, len(src_lines), len(dst_lines))):
        src = src_lines[i]
        dst = dst_lines[i]
        
        # Solo mostrar si son diferentes pero deberían ser traducidas
        if (src != dst and 
            len(src) > 20 and 
            not src.startswith(('//', ':', '[', '|', '----', 'include')) and
            not re.match(r'^=+\s', src)):
            
            print(f"  Línea {i+1}:")
            print(f"    Original:  {src[:80]}...")
            print(f"    Traducido: {dst[:80]}...")
            print()
    
    return 0 if src_translatable == dst_translatable else 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: test_translation.py <directorio_original> <directorio_traducido>")
        sys.exit(1)
    
    src_dir = Path(sys.argv[1])
    dst_dir = Path(sys.argv[2])
    
    print("=== PRUEBA DE TRADUCCIÓN ===")
    print(f"Directorio original: {src_dir}")
    print(f"Directorio traducido: {dst_dir}")
    
    total_files = 0
    total_issues = 0
    
    for src_file in src_dir.rglob("*.adoc"):
        rel_path = src_file.relative_to(src_dir)
        dst_file = dst_dir / rel_path
        
        if dst_file.exists():
            total_files += 1
            total_issues += check_translation(src_file, dst_file)
    
    print(f"\n=== RESUMEN ===")
    print(f"Archivos procesados: {total_files}")
    print(f"Archivos con problemas: {total_issues}")
    
    if total_issues == 0:
        print("Todas las traducciones parecen correctas")
    else:
        print(f"{total_issues} archivos pueden tener problemas")