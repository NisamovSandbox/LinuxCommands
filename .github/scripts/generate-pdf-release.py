#!/usr/bin/env python3
import subprocess
from pathlib import Path

ROOT_DIR = Path(".")
OUTPUT_DIR = ROOT_DIR / "output"
EXCLUDE_DIRS = {ROOT_DIR / ".github", OUTPUT_DIR}

OUTPUT_DIR.mkdir(exist_ok=True)

PANDOC_BASE_CMD = [
    "pandoc",
    "--pdf-engine=lualatex",
    "-V", "lang=es-ES",
    "-V", "geometry:margin=1.5cm",
    "-V", "fontsize=11pt"
]

def gather_files(directory: Path):
    files = []

    readme = directory / "README.md"
    if readme.exists():
        files.append(readme)

    for ext in (".md", ".yml", ".yaml", ".conf"):
        for f in sorted(directory.glob(f"*{ext}")):
            if f.name != "README.md":
                files.append(f)

    for subdir in sorted(
        d for d in directory.iterdir()
        if d.is_dir() and d not in EXCLUDE_DIRS
    ):
        files.extend(gather_files(subdir))

    return files

def render_to_image(src_file: Path) -> Path:
    # Nombre único para evitar colisiones entre carpetas
    img_name = f"{src_file.parent.name}_{src_file.stem}.png"
    output_img = OUTPUT_DIR / img_name

    subprocess.run([
        "silicon",
        str(src_file),
        "--font", "Noto Sans Mono",
        "--background", "#ffffff",
        "--no-line-number",
        "--pad-horiz", "40",
        "--pad-vert", "20",
        "--line-pad", "6",
        "--output", str(output_img)
    ], check=True)

    return output_img

def generate_pdf(directory: Path):
    files = gather_files(directory)
    if not files:
        return

    temp_md = OUTPUT_DIR / f"{directory.name}_temp.md"
    output_pdf = OUTPUT_DIR / f"{directory.name.upper()}.pdf"

    with temp_md.open("w", encoding="utf-8") as out_md:
        for i, f in enumerate(files):
            img = render_to_image(f)
            out_md.write(f"![]({img.name})\n")

            if i < len(files) - 1:
                out_md.write("\\newpage\n")

    cmd = PANDOC_BASE_CMD + [
        str(temp_md.resolve()),
        "-V", "documentclass=article",
        "-V", "classoption=landscape",
        "-o", str(output_pdf.resolve())
    ]

    subprocess.run(cmd, check=True)
    temp_md.unlink()

def main():
    for item in ROOT_DIR.iterdir():
        if item.is_dir() and item not in EXCLUDE_DIRS:
            generate_pdf(item)

if __name__ == "__main__":
    main()
