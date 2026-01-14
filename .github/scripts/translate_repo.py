import os
from concurrent.futures import ThreadPoolExecutor
import deepl
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
EXTENSIONS = (".md", ".conf", ".adoc")
OUTPUT_DIR = "translated_repo"
def translate_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    translated_text = translator.translate_text(content, target_lang="EN-US").text
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(translated_text)
file_paths = []
for root, _, files in os.walk("."):
    if OUTPUT_DIR in root:
        continue
    for file in files:
        if file.endswith(EXTENSIONS):
            input_path = os.path.join(root, file)
            rel_path = os.path.relpath(input_path, ".")
            output_path = os.path.join(OUTPUT_DIR, rel_path)
            file_paths.append((input_path, output_path))
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(lambda p: translate_file(p[0], p[1]), file_paths)