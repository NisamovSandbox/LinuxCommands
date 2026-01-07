#!/usr/bin/env python3
import re
from pathlib import Path
EXCLUDED_DIRS = {'.git', '.github', '__pycache__'}
EXCLUDED_FILES = {'README.md', 'CONTRIBUTING.md', 'INFO.md', 'KEYWORD.md', 'LICENSE'}
ROOT = Path('.')
def generate_index(path: Path, include_files=True, depth=0):
    lines = []
    for item in sorted(path.iterdir(), key=lambda x: x.name):
        if item.name in EXCLUDED_DIRS:
            continue

        indent = '  ' * depth
        if item.is_dir():
            lines.append(f"{indent}- [{item.name}](/{item.as_posix()})")
        elif include_files and item.suffix == '.md' and item.name not in EXCLUDED_FILES:
            lines.append(f"{indent}- [{item.name}](/{item.as_posix()})")
    return lines
def write_readme(path: Path, lines):
    readme = path / 'README.md'
    start = '<!-- AUTO-GENERATED-INDEX:START -->'
    end = '<!-- AUTO-GENERATED-INDEX:END -->'
    tree_md = '\n'.join(lines)
    new_block = f"{start}\n{tree_md}\n{end}"
    if readme.exists():
        content = readme.read_text(encoding='utf-8')
        pattern = re.compile(re.escape(start) + '.*?' + re.escape(end), re.DOTALL)
        updated = pattern.sub(new_block, content)
    else:
        updated = f"# {path.name}\n\n{new_block}"
    readme.write_text(updated, encoding='utf-8')
def generate_readmes(path: Path, is_root=True):
    if is_root:
        lines = generate_index(path, include_files=False, depth=0)
    else:
        lines = generate_index(path, include_files=True, depth=0)
    write_readme(path, lines)
    for item in path.iterdir():
        if item.is_dir() and item.name not in EXCLUDED_DIRS:
            generate_readmes(item, is_root=False)
if __name__ == '__main__':
    generate_readmes(ROOT)
