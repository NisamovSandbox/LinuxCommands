import os
import deepl
import re

translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
#EXTENSIONS = (".md", ".conf", ".adoc")
EXTENSIONS = (".md") # Limitado para pruebas

def translate_preserving_indent(text):
    lines = text.splitlines(keepends=True)
    result = []

    for line in lines:
        match = re.match(r"^(\s*)(.*)", line)
        indent, content = match.groups()

        if not content.strip():
            result.append(line)
            continue

        translated = translator.translate_text(
            content,
            source_lang="ES",
            target_lang="EN-US"
        ).text

        result.append(indent + translated + ("\n" if line.endswith("\n") else ""))

    return "".join(result)

def translate_file(path):
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    translated = translate_preserving_indent(original)

    if translated != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(translated)

for root, _, files in os.walk("."):
    if ".git" in root:
        continue
    for file in files:
        if file.endswith(EXTENSIONS):
            translate_file(os.path.join(root, file))
