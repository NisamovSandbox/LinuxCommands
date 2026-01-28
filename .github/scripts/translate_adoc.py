#!/usr/bin/env python3
from pathlib import Path
from deep_translator import GoogleTranslator
import sys
import time
if len(sys.argv) != 3:
    print("Uso: translate_adoc.py <SRC_DIR> <DST_DIR>")
    sys.exit(1)
SRC_ROOT = Path(sys.argv[1])
DST_ROOT = Path(sys.argv[2])
DST_ROOT.mkdir(parents=True, exist_ok=True)
translator = GoogleTranslator(source="es", target="en")
def should_translate(line: str) -> bool:
    stripped = line.lstrip()
    if stripped.startswith((
        "=",          # títulos
        ":",          # atributos
        "include::",  # includes
        "[source",    # bloques
        "----",       # delimitadores
        "ifdef::",
        "ifndef::",
        "ifeval::",
        "//",         # comentarios
    )):
        return False
    if stripped.strip() == "":
        return False
    return True
def translate_adoc(text: str) -> str:
    output = []
    in_code_block = False
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        prefix = ""
        if stripped.startswith("* "):
            prefix = "* "
            line_to_translate = stripped[2:]
        else:
            line_to_translate = line.rstrip("\n")
        if stripped.startswith("----"):
            in_code_block = not in_code_block
            output.append(line)
            continue
        if in_code_block:
            output.append(line)
            continue
        if should_translate(line):
            try:
                translated = translator.translate(line.rstrip("\n"))
                output.append(translated + "\n")
                time.sleep(0.05)
            except Exception as e:
                output.append(line)
        else:
            output.append(line)
    return "".join(output)
for src_file in SRC_ROOT.rglob("*.adoc"):
    relative_path = src_file.relative_to(SRC_ROOT)
    dst_file = DST_ROOT / relative_path
    dst_file.parent.mkdir(parents=True, exist_ok=True)
    text = src_file.read_text(encoding="utf-8")
    translated_text = translate_adoc(text)
    dst_file.write_text(translated_text, encoding="utf-8")
    print(f"Traducido: {src_file} -> {dst_file}")