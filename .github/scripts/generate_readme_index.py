#!/usr/bin/env python3
from pathlib import Path
# Directorios y ficheros excluidos
EXCLUDED_DIRS = {'.git', '.github', '__pycache__'}
EXCLUDED_FILES = {
    'README.md',
    'CONTRIBUTING.md',
    'INFO.md',
    'KEYWORD.md',
    'LICENSE'
}
ROOT = Path('.')
START = '<!-- AUTO-GENERATED-INDEX:START -->'
END   = '<!-- AUTO-GENERATED-INDEX:END -->'
def write_readme(path: Path, lines: list[str]) -> None:
    """
    Inserta o reemplaza el bloque AUTO-GENERATED-INDEX en el README.md
    del directorio indicado, sin usar regex (robusto frente a HTML).
    """
    readme = path / 'README.md'
    block = f"{START}\n" + "\n".join(lines) + f"\n{END}"
    if readme.exists():
        content = readme.read_text(encoding='utf-8')
        if START in content and END in content:
            before, _, rest = content.partition(START)
            _, _, after = rest.partition(END)
            content = before + block + after
        else:
            content = content.rstrip() + "\n\n" + block
    else:
        content = f"# {path.name}\n\n{block}"
    readme.write_text(content, encoding='utf-8')
# README principal: solo directorios de primer nivel que contienen README.md en subdirectorios
def has_nested_readme(dirpath: Path) -> bool:
    for sub in dirpath.iterdir():
        if (
            sub.is_dir()
            and sub.name not in EXCLUDED_DIRS
            and (sub / 'README.md').exists()
        ):
            return True
    return False
def generate_root_readme() -> None:
    lines = []
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or d.name in EXCLUDED_DIRS:
            continue
        if has_nested_readme(d):
            lines.append(f"- [{d.name}](/{d.name})")
    write_readme(ROOT, lines)
# README de secciones: subdirectorios + ficheros markdown
def generate_section_readme(section: Path) -> None:
    lines = []
    # Subdirectorios
    for d in sorted(section.iterdir()):
        if not d.is_dir() or d.name in EXCLUDED_DIRS:
            continue
        lines.append(f"- [{d.name}](/{d.as_posix()})")
        for f in sorted(d.glob('*.md')):
            if f.name in EXCLUDED_FILES:
                continue
            rel = f.relative_to(section).as_posix()
            lines.append(f"  - [{rel}](/{f.as_posix()})")
    # Ficheros markdown del propio nivel
    for f in sorted(section.glob('*.md')):
        if f.name in EXCLUDED_FILES:
            continue
        lines.append(f"- [{f.name}](/{f.as_posix()})")

    write_readme(section, lines)
# Main
if __name__ == '__main__':
    generate_root_readme()

    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name not in EXCLUDED_DIRS:
            generate_section_readme(d)
