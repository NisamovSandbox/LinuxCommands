#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

# Configuración
ROOT_DIR = Path(".")
OUTPUT_DIR = ROOT_DIR / "output"
EXCLUDE_DIRS = [ROOT_DIR / ".github"]
OUTPUT_DIR.mkdir(exist_ok=True)

# Fuente y opciones para XeLaTeX
PANDOC_BASE_CMD = [
    "pandoc",
    "--pdf-engine=xelatex",
    "-V", "lang=es-ES",
    "-V", "mainfont=Noto Sans",
    "-V", "sansfont=Noto Sans",
    "-V", "monofont=Noto Sans Mono",
    "-V", "mainfontoptions=Renderer=Harfbuzz",
    "-V", "monofontoptions=Renderer=Harfbuzz",
    "-V", "geometry:margin=1.5cm"
]

def gather_files(directory: Path):
    """Recoge los archivos según orden: README.md -> otros .md -> .yml/.yaml -> .conf"""
    readme = directory / "README.md"
    files = []

    # README.md primero
    if readme.exists():
        files.append(readme)

    # Otros archivos por extensión
    exts_order = [".md", ".yml", ".yaml", ".conf"]
    for ext in exts_order:
        for f in sorted(directory.glob(f"*{ext}")):
            if f.name != "README.md":
                files.append(f)
    
    # Subdirectorios
    for subdir in sorted([d for d in directory.iterdir() if d.is_dir() and d not in EXCLUDE_DIRS]):
        files.extend(gather_files(subdir))
    
    return files

def generate_pdf(directory: Path):
    """Genera el PDF de un directorio"""
    files = gather_files(directory)
    if not files:
        return
    
    output_file = OUTPUT_DIR / f"{directory.name.upper()}.pdf"

    # Crear archivo temporal con Markdown concatenado
    temp_md = OUTPUT_DIR / f"{directory.name}_temp.md"
    with open(temp_md, "w", encoding="utf-8") as out_md:
        for f in files:
            out_md.write(f"# {f.name}\n\n")
            # Comandos en horizontal
            if f.name == "commands.md":
                # PDF horizontal para commands.md
                cmd = PANDOC_BASE_CMD + [
                    "-V", "documentclass=article",
                    "-V", "classoption=landscape",
                    str(f),
                    "-o", str(OUTPUT_DIR / f"{directory.name.upper()}_COMMANDS.pdf")
                ]
                subprocess.run(cmd, check=True)
            else:
                # Markdown normal o conf/yaml
                if f.suffix in [".yaml", ".yml", ".conf"]:
                    out_md.write("```\n")
                    out_md.write(f.read_text(encoding="utf-8"))
                    out_md.write("\n```\n\n")
                else:
                    out_md.write(f.read_text(encoding="utf-8"))
                    out_md.write("\n\n")

    # Generar PDF principal
    cmd = PANDOC_BASE_CMD + [
        str(temp_md),
        "-V", "documentclass=article",
        "-V", "classoption=portrait",
        "-o", str(output_file)
    ]
    subprocess.run(cmd, check=True)
    temp_md.unlink()  # borrar temporal

def main():
    # Recorrer todos los subdirectorios de la raíz
    for item in ROOT_DIR.iterdir():
        if item.is_dir() and item not in EXCLUDE_DIRS:
            generate_pdf(item)

if __name__ == "__main__":
    main()
