#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from transformers import MarianMTModel, MarianTokenizer
from multiprocessing import Pool, cpu_count

MODEL_NAME = "Helsinki-NLP/opus-mt-es-en"
tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

def translate_text(text: str) -> str:
    batch = tokenizer([text], return_tensors="pt", truncation=True, padding=True)
    generated = model.generate(**batch)
    return tokenizer.decode(generated[0], skip_special_tokens=True)

def extract_code_blocks(text: str) -> (str, dict):
    code_blocks = {}
    for i, match in enumerate(re.findall(r"```.*?```", text, flags=re.DOTALL)):
        placeholder = f"__CODE_BLOCK_MD_{i}__"
        code_blocks[placeholder] = match
        text = text.replace(match, placeholder)
    for i, match in enumerate(re.findall(r"\\begin\{.*?\}.*?\\end\{.*?\}", text, flags=re.DOTALL)):
        placeholder = f"__CODE_BLOCK_TEX_{i}__"
        code_blocks[placeholder] = match
        text = text.replace(match, placeholder)
    for i, match in enumerate(re.findall(r"(\[source.*?\]\n----.*?----)", text, flags=re.DOTALL)):
        placeholder = f"__CODE_BLOCK_ADOC_{i}__"
        code_blocks[placeholder] = match
        text = text.replace(match, placeholder)
    return text, code_blocks

def restore_code_blocks(text: str, code_blocks: dict) -> str:
    for placeholder, code in code_blocks.items():
        text = text.replace(placeholder, code)
    return text

def translate_paragraphs(text: str) -> str:
    paragraphs = text.split("\n\n")
    translated_paragraphs = []
    for p in paragraphs:
        if not p.strip():
            translated_paragraphs.append(p)
            continue
        leading_spaces = len(p) - len(p.lstrip(' '))
        translated = translate_text(p.strip())
        translated_paragraphs.append(' ' * leading_spaces + translated)
    return "\n\n".join(translated_paragraphs)

def translate_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content, code_blocks = extract_code_blocks(content)
    translated = translate_paragraphs(content)
    translated = restore_code_blocks(translated, code_blocks)

    with open(path, "w", encoding="utf-8") as f:
        f.write(translated)
    print(f"[OK] Traducido {path}")

def collect_files(extensions=(".md", ".tex", ".adoc")):
    files_to_translate = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(extensions):
                files_to_translate.append(os.path.join(root, file))
    return files_to_translate

def main():
    files = collect_files()
    cpu = min(cpu_count(), len(files))
    with Pool(cpu) as pool:
        pool.map(translate_file, files)

if __name__ == "__main__":
    main()
