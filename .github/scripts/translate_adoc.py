#!/usr/bin/env python3
from pathlib import Path
from deep_translator import GoogleTranslator
import sys
MAX_LEN = 4000
def chunks(text, size=MAX_LEN):
    for i in range(0, len(text), size):
        yield text[i:i+size]
SRC_ROOT = Path(sys.argv[1])
DST_ROOT = Path(sys.argv[2])
DST_ROOT.mkdir(exist_ok=True, parents=True)
for src_file in SRC_ROOT.rglob("*.adoc"):
    relative_path = src_file.relative_to(SRC_ROOT)
    dst_file = DST_ROOT / relative_path
    dst_file.parent.mkdir(parents=True, exist_ok=True)
    text = src_file.read_text(encoding="utf-8")
    translated_text = ""
    for part in chunks(text):
        translated_text += GoogleTranslator(source='es', target='en').translate(part)
    dst_file.write_text(translated_text, encoding="utf-8")
    print(f"Traducido: {src_file} -> {dst_file}")
