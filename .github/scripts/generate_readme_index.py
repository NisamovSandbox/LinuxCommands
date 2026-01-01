#!/usr/bin/env python3
import re
from pathlib import Path

EXCLUDED_DIRS = {
    '.git',
    '.github',
    '__pycache__'
}

EXCLUDED_FILES = {
    'README.md',
    'CONTRIBUTING.md',
    'INFO.md',
    'KEYWORD.md',
    'LICENSE'
}

ROOT = Path('.')

def generate_tree(path: Path, depth: int = 0):
    lines = []

    for item in sorted(path.iterdir(), key=lambda x: x.name):
        if item.name in EXCLUDED_DIRS:
            continue

        if item.is_dir():
            indent = '  ' * depth
            lines.append(f"{indent}- {item.name}")
            lines.extend(generate_tree(item, depth + 1))

        elif (
            item.is_file()
            and item.suffix == '.md'
            and item.name not in EXCLUDED_FILES
        ):
            indent = '  ' * depth
            rel_path = item.as_posix()
            lines.append(f"{indent}- [{item.name}](/{rel_path})")

    return lines


def update_readme(tree_md: str):
    readme = Path('README.md')

    if not readme.exists():
        raise FileNotFoundError("README.md no encontrado")

    content = readme.read_text(encoding='utf-8')

    start = '<!-- AUTO-GENERATED-INDEX:START -->'
    end = '<!-- AUTO-GENERATED-INDEX:END -->'

    pattern = re.compile(
        re.escape(start) + '.*?' + re.escape(end),
        re.DOTALL
    )

    new_block = f"{start}\n{tree_md}\n{end}"

    updated = pattern.sub(new_block, content)

    readme.write_text(updated, encoding='utf-8')


if __name__ == '__main__':
    tree = '\n'.join(generate_tree(ROOT))
    update_readme(tree)
