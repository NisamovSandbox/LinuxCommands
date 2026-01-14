import os
import deepl
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
EXTENSIONS = (".md", ".conf", ".adoc")
OUTPUT_DIR = "translated_repo"
def translate_line_preserve_indent(line):
    leading_spaces = len(line) - len(line.lstrip(" \t"))
    indent = line[:leading_spaces]
    text = line.lstrip(" \t")
    if text.strip() == "":
        return line
    translated = translator.translate_text(text, target_lang="EN-US").text
    return indent + translated
def translate_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    translated_lines = [translate_line_preserve_indent(line) for line in lines]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(translated_lines)
for root, _, files in os.walk("."):
    if OUTPUT_DIR in root:
        continue
    for file in files:
        if file.endswith(EXTENSIONS):
            input_path = os.path.join(root, file)
            rel_path = os.path.relpath(input_path, ".")
            output_path = os.path.join(OUTPUT_DIR, rel_path)
            translate_file(input_path, output_path)