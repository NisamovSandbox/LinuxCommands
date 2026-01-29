#!/usr/bin/env python3
from pathlib import Path
from deep_translator import GoogleTranslator
import sys
import time
import re
import html

if len(sys.argv) != 4:
    print("Uso: translate_adoc.py <SRC_DIR> <DST_DIR> <TARGET_LANG>")
    sys.exit(1)

SRC_ROOT = Path(sys.argv[1])
DST_ROOT = Path(sys.argv[2])
TARGET_LANG = sys.argv[3]
DST_ROOT.mkdir(parents=True, exist_ok=True)

translator = GoogleTranslator(source="auto", target=TARGET_LANG)

# Patrones más precisos
CODE_BLOCK_DELIM = re.compile(r'^----\s*$')
SOURCE_BLOCK = re.compile(r'^\[source')
TABLE_BLOCK = re.compile(r'^\|===')
COMMENT_LINE = re.compile(r'^\s*//')
INCLUDE_DIRECTIVE = re.compile(r'^include::')
ATTRIBUTE_DEF = re.compile(r'^:[\w-]+:')
HEADER_LINE = re.compile(r'^=+[\s\w]')
MACRO_LINE = re.compile(r'^\[.*\]\s*$')
LIST_ITEM = re.compile(r'^\s*[\*\-+]\s+')
ENUM_ITEM = re.compile(r'^\s*\d+\.\s+')

def should_translate_line(line: str) -> bool:
    """Determina si una línea completa debe ser traducida"""
    stripped = line.rstrip()
    
    # Línea vacía
    if not stripped:
        return False
    
    # Comentarios
    if COMMENT_LINE.match(stripped):
        return False
    
    # Directivas includes
    if INCLUDE_DIRECTIVE.match(stripped):
        return False
    
    # Definiciones de atributos
    if ATTRIBUTE_DEF.match(stripped):
        return False
    
    # Bloques de código fuente
    if SOURCE_BLOCK.match(stripped):
        return False
    
    # Tablas
    if TABLE_BLOCK.match(stripped):
        return False
    
    # Líneas que son solo macros
    if MACRO_LINE.match(stripped):
        return False
    
    return True

def extract_translatable_text(line: str) -> tuple[str, str, str]:
    """
    Extrae texto traducible de una línea.
    Devuelve: (prefijo, texto_a_traducir, sufijo)
    """
    stripped = line.rstrip()
    
    # Elementos de lista
    list_match = LIST_ITEM.match(line)
    if list_match:
        prefix = list_match.group(0)
        text = line[len(prefix):].rstrip()
        return prefix, text, ""
    
    # Elementos enumerados
    enum_match = ENUM_ITEM.match(line)
    if enum_match:
        prefix = enum_match.group(0)
        text = line[len(prefix):].rstrip()
        return prefix, text, ""
    
    # Para otras líneas, intentar preservar indentación
    leading_spaces = len(line) - len(line.lstrip())
    prefix = line[:leading_spaces]
    text = line[leading_spaces:].rstrip()
    
    return prefix, text, ""

def translate_text(text: str) -> str:
    """Traduce texto con manejo de errores"""
    if not text or not text.strip():
        return text
    
    # Limitar longitud para evitar errores de la API
    if len(text) > 4500:
        chunks = []
        # Dividir en párrafos si es posible
        paragraphs = text.split('\n\n')
        for para in paragraphs:
            if len(para) > 4500:
                # Dividir por oraciones
                sentences = re.split(r'(?<=[.!?])\s+', para)
                chunk = ""
                for sentence in sentences:
                    if len(chunk) + len(sentence) < 4500:
                        chunk += sentence + " "
                    else:
                        if chunk:
                            chunks.append(chunk.strip())
                        chunk = sentence + " "
                if chunk:
                    chunks.append(chunk.strip())
            else:
                chunks.append(para)
    else:
        chunks = [text]
    
    translated_chunks = []
    for chunk in chunks:
        if not chunk.strip():
            translated_chunks.append("")
            continue
            
        try:
            # Escapar HTML antes de traducir
            chunk_clean = html.escape(chunk) if '<' in chunk or '>' in chunk else chunk
            
            translated = translator.translate(chunk_clean)
            if translated and translated != chunk_clean:
                # Desescapar HTML si es necesario
                if '&' in translated:
                    translated = html.unescape(translated)
                translated_chunks.append(translated)
            else:
                translated_chunks.append(chunk)
            
            # Pequeña pausa entre traducciones
            time.sleep(0.2)
        except Exception as e:
            print(f"  Error traduciendo texto: {str(e)[:100]}")
            translated_chunks.append(chunk)
            time.sleep(1)  # Pausa más larga si hay error
    
    return '\n\n'.join(translated_chunks)

def translate_adoc(content: str) -> str:
    """Traduce contenido AsciiDoc manteniendo estructura"""
    lines = content.splitlines()
    translated_lines = []
    
    in_code_block = False
    in_table = False
    buffer = []
    current_indent = ""
    
    for i, line in enumerate(lines):
        original_line = line
        
        # Detectar bloques de código
        if CODE_BLOCK_DELIM.match(line.rstrip()):
            in_code_block = not in_code_block
            translated_lines.append(line)
            continue
        
        if in_code_block:
            translated_lines.append(line)
            continue
        
        # Detectar tablas
        if TABLE_BLOCK.match(line.rstrip()):
            in_table = not in_table
            translated_lines.append(line)
            continue
        
        if in_table:
            translated_lines.append(line)
            continue
        
        # Verificar si la línea debe ser traducida
        if not should_translate_line(line):
            translated_lines.append(line)
            continue
        
        # Extraer texto traducible
        prefix, text, suffix = extract_translatable_text(line)
        
        if text:
            try:
                translated_text = translate_text(text)
                if translated_text:
                    translated_lines.append(prefix + translated_text + suffix)
                else:
                    translated_lines.append(line)
            except Exception as e:
                print(f"  Error en línea {i+1}: {str(e)[:50]}")
                translated_lines.append(line)
        else:
            translated_lines.append(line)
    
    return '\n'.join(translated_lines)

def process_file(src_file: Path, dst_file: Path):
    """Procesa un archivo .adoc individual"""
    print(f"Procesando: {src_file}")
    
    try:
        # Leer contenido
        text = src_file.read_text(encoding="utf-8")
        
        # Verificar si el archivo tiene contenido
        if not text.strip():
            print(f"  Archivo vacío, copiando sin cambios")
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            dst_file.write_text(text, encoding="utf-8")
            return
        
        # Traducir
        print(f"  Traduciendo {len(text)} caracteres...")
        translated_text = translate_adoc(text)
        
        # Escribir archivo traducido
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        dst_file.write_text(translated_text, encoding="utf-8")
        
        print(f"  ✓ Traducido a {TARGET_LANG}: {dst_file}")
        
    except Exception as e:
        print(f"  ✗ ERROR procesando {src_file}: {str(e)}")
        # Copiar el archivo original si hay error
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        try:
            dst_file.write_text(src_file.read_text(encoding="utf-8"), encoding="utf-8")
        except:
            dst_file.write_text("")

# Procesar todos los archivos .adoc
adoc_files = list(SRC_ROOT.rglob("*.adoc"))
print(f"\nEncontrados {len(adoc_files)} archivos .adoc para traducir")

for i, src_file in enumerate(adoc_files, 1):
    relative_path = src_file.relative_to(SRC_ROOT)
    dst_file = DST_ROOT / relative_path
    
    print(f"\n[{i}/{len(adoc_files)}] ", end="")
    process_file(src_file, dst_file)
    
    # Pausa ocasional para evitar sobrecargar la API
    if i % 10 == 0:
        print("  Pausando 2 segundos...")
        time.sleep(2)

print(f"\nTraducción completada. Archivos {TARGET_LANG} guardados en: {DST_ROOT}")