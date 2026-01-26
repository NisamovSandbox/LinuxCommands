#!/usr/bin/env python3
from pathlib import Path
from googletrans import Translator

import sys

translator = Translator()

SRC_ROOT = Path(sys.argv[1])   # Carpeta de origen (español)
DST_ROOT = Path(sys.argv[2])   # Carpeta destino (inglés)
DST_ROOT.mkdir(exist_ok=True, parents=True)

for src_file in SRC_ROOT.rglob("*.adoc"):
    relative_path = src_file.relative_to(SRC_ROOT)
    dst_file = DST_ROOT / relative_path
    dst_file.parent.mkdir(parents=True, exist_ok=True)
    
    text = src_file.read_text(encoding="utf-8")
    translated = translator.translate(text, src='es', dest='en').text
    dst_file.write_text(translated, encoding="utf-8")
    print(f"Traducido: {src_file} -> {dst_file}")
