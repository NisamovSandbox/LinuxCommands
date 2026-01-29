#!/usr/bin/env python3
from pathlib import Path
from deep_translator import GoogleTranslator
import sys
import time
import re

if len(sys.argv) != 4:
    print("Uso: translate_adoc.py <SRC_DIR> <DST_DIR> <TARGET_LANG>")
    sys.exit(1)

SRC_ROOT = Path(sys.argv[1])
DST_ROOT = Path(sys.argv[2])
TARGET_LANG = sys.argv[3]
DST_ROOT.mkdir(parents=True, exist_ok=True)

translator = GoogleTranslator(source="es", target=TARGET_LANG)

# Patrones más específicos para detectar contenido que NO debe traducirse
CODE_BLOCK_START = re.compile(r'^\[source,.*\]$')
UNORDERED_BLOCK = re.compile(r'^\[unordered\.stack\]$')
COMMENT_LINE = re.compile(r'^//')
DIRECTIVE_LINE = re.compile(r'^(include|ifdef|ifndef|ifeval)::')
ATTRIBUTE_LINE = re.compile(r'^:[\w-]+:')
HEADER_LINE = re.compile(r'^=+ ')
MACRO_LINE = re.compile(r'^\[.*\]$')  # Líneas que son solo atributos entre corchetes

def should_translate(line: str) -> bool:
    stripped = line.strip()
    
    # Si está vacía
    if not stripped:
        return False
    
    # Si es un comentario
    if COMMENT_LINE.match(stripped):
        return False
    
    # Si es una directiva de AsciiDoc
    if DIRECTIVE_LINE.match(stripped):
        return False
    
    # Si es una línea de atributo
    if ATTRIBUTE_LINE.match(stripped):
        return False
    
    # Si es un encabezado
    if HEADER_LINE.match(stripped):
        return False
    
    # Si es un bloque de código o lista especial
    if CODE_BLOCK_START.match(stripped) or UNORDERED_BLOCK.match(stripped):
        return False
    
    # Si es solo una línea de atributos entre corchetes
    if MACRO_LINE.match(stripped):
        return False
    
    # Si contiene marcadores de AsciiDoc que no deben traducirse
    if any(marker in stripped for marker in [
        "::", "xref:", "link:", "image::", "footnote:",
        "<<", ">>", "pass:", "icon:", "btn:"
    ]):
        return False
    
    # Si es un elemento de lista (pero queremos traducir el texto después del marcador)
    if stripped.startswith(("* ", "- ", "+ ")):
        # Traducir solo el texto después del marcador
        return True
    
    return True

def translate_text(text: str, max_length: int = 4500) -> str:
    """Traduce texto con manejo de límites de caracteres"""
    if len(text) <= max_length:
        try:
            return translator.translate(text)
        except Exception as e:
            print(f"Error traduciendo texto largo: {e}")
            return text
    
    # Dividir texto largo en chunks
    chunks = []
    current_chunk = ""
    sentences = text.split('. ')
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 2 <= max_length:
            current_chunk += sentence + '. '
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = sentence + '. '
    
    if current_chunk:
        chunks.append(current_chunk)
    
    # Traducir cada chunk
    translated_chunks = []
    for chunk in chunks:
        try:
            translated = translator.translate(chunk)
            translated_chunks.append(translated)
            time.sleep(0.1)  # Pequeña pausa para evitar rate limiting
        except Exception as e:
            print(f"Error traduciendo chunk: {e}")
            translated_chunks.append(chunk)
    
    return ' '.join(translated_chunks)

def translate_adoc(text: str) -> str:
    output = []
    in_code_block = False
    in_unordered_block = False
    lines = text.splitlines()
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Manejar bloques de código
        if line.strip() == "----":
            in_code_block = not in_code_block
            output.append(line)
            i += 1
            continue
        
        if in_code_block:
            output.append(line)
            i += 1
            continue
        
        # Manejar bloques unordered.stack
        if line.strip() == "[unordered.stack]":
            in_unordered_block = True
            output.append(line)
            i += 1
            # Procesar las líneas siguientes que son parte del bloque
            while i < len(lines) and (lines[i].startswith("-") or lines[i].strip() == ""):
                # Para elementos de lista como "-~:: `cd ~` Ir al directorio..."
                if lines[i].startswith("-") and "::" in lines[i]:
                    parts = lines[i].split("::", 1)
                    if len(parts) == 2:
                        marker = parts[0].strip()
                        content = parts[1].strip()
                        # Solo traducir la parte descriptiva (después del código)
                        if "`" in content:
                            # Separar código y descripción
                            code_end = content.rfind("`")
                            if code_end != -1:
                                code_part = content[:code_end+1]
                                desc_part = content[code_end+1:]
                                if desc_part.strip():
                                    try:
                                        translated_desc = translator.translate(desc_part.strip())
                                        output.append(f"{marker}:: {code_part} {translated_desc}")
                                    except Exception:
                                        output.append(lines[i])
                                else:
                                    output.append(lines[i])
                            else:
                                output.append(lines[i])
                        else:
                            try:
                                translated_content = translator.translate(content)
                                output.append(f"{marker}:: {translated_content}")
                            except Exception:
                                output.append(lines[i])
                    else:
                        output.append(lines[i])
                else:
                    output.append(lines[i])
                i += 1
            in_unordered_block = False
            continue
        
        # Procesar línea normal
        if should_translate(line):
            if line.startswith(("* ", "- ", "+ ")):
                # Para elementos de lista, traducir solo después del marcador
                marker = line[:2]
                content = line[2:]
                if content.strip():
                    try:
                        translated_content = translate_text(content.strip())
                        output.append(f"{marker}{translated_content}")
                    except Exception:
                        output.append(line)
                else:
                    output.append(line)
            else:
                # Para texto normal
                if line.strip():
                    try:
                        translated_line = translate_text(line.strip())
                        output.append(translated_line)
                    except Exception:
                        output.append(line)
                else:
                    output.append(line)
        else:
            output.append(line)
        
        i += 1
    
    return "\n".join(output)

def process_file(src_file: Path, dst_file: Path):
    """Procesa un archivo .adoc individual"""
    print(f"Procesando: {src_file}")
    
    # Leer contenido
    text = src_file.read_text(encoding="utf-8")
    
    # Traducir
    translated_text = translate_adoc(text)
    
    # Escribir archivo traducido
    dst_file.parent.mkdir(parents=True, exist_ok=True)
    dst_file.write_text(translated_text, encoding="utf-8")
    
    print(f"  Traducido a {TARGET_LANG}: {dst_file}")

# Procesar todos los archivos .adoc
for src_file in SRC_ROOT.rglob("*.adoc"):
    relative_path = src_file.relative_to(SRC_ROOT)
    dst_file = DST_ROOT / relative_path
    process_file(src_file, dst_file)

print(f"\nTraducción completada. Archivos {TARGET_LANG} guardados en: {DST_ROOT}")