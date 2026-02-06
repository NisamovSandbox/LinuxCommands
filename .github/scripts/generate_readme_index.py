#!/usr/bin/env python3
from pathlib import Path
from typing import List

ROOT = Path('.')

EXCLUDED_DIRS = {
    '.git',
    '.github',
    'docs',
    '__pycache__'
}

START = '<!-- AUTO-GENERATED-INDEX:START -->'
END   = '<!-- AUTO-GENERATED-INDEX:END -->'


def write_readme(lines: List[str]) -> None:
    readme = ROOT / 'README.md'

    if not readme.exists():
        raise RuntimeError('README.md no encontrado en la raíz')

    content = readme.read_text(encoding='utf-8')

    if START not in content or END not in content:
        raise RuntimeError('Bloque AUTO-GENERATED-INDEX no encontrado')

    block = f"{START}\n" + "\n".join(lines) + f"\n{END}"

    before, _, rest = content.partition(START)
    _, _, after = rest.partition(END)

    new_content = before + block + after
    readme.write_text(new_content, encoding='utf-8')


def generate_root_structure() -> None:
    lines: List[str] = []

    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name not in EXCLUDED_DIRS:
            lines.append(f"- [{d.name}](/{d.name})")

    write_readme(lines)


if __name__ == '__main__':
    generate_root_structure()
