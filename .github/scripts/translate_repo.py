import os
import subprocess
import argostranslate.package
import argostranslate.translate
import tempfile
import shutil

# Instalar paquete español → inglés si no está
available_packages = argostranslate.package.get_available_packages()
es_en_package = None
for package in available_packages:
    if package.from_code == "es" and package.to_code == "en":
        es_en_package = package
        break

if es_en_package:
    with tempfile.TemporaryDirectory() as tmpdir:
        package_path = es_en_package.download()
        argostranslate.package.install_from_path(package_path)

# Cargar idiomas instalados
installed_languages = argostranslate.translate.get_installed_languages()
es_lang = next(l for l in installed_languages if l.code == "es")
en_lang = next(l for l in installed_languages if l.code == "en")
translation = es_lang.get_translation(en_lang)

# Carpeta temporal para traducción
temp_dir = "translated_repo"

if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
shutil.copytree(".", temp_dir, ignore=shutil.ignore_patterns(".git", ".github"))

def translate_file(path: str):
    """Traduce respetando sangrías y bloques de código"""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    translated_lines = []
    in_code_block = False
    for line in lines:
        stripped = line.strip()

        # Detectar bloques de código (``` o indentación de 4 espacios)
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            translated_lines.append(line)
            continue
        if in_code_block or line.startswith("    "):
            # No traducir líneas de código
            translated_lines.append(line)
            continue

        if stripped:
            translated_line = translation.translate(stripped)
            leading_spaces = len(line) - len(line.lstrip(" "))
            translated_lines.append(" " * leading_spaces + translated_line + "\n")
        else:
            translated_lines.append("\n")

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(translated_lines)

# Traducir todos los archivos relevantes
for root, _, files in os.walk(temp_dir):
    for file in files:
        if file.endswith((".md", ".txt", ".adoc")):
            translate_file(os.path.join(root, file))

# Commit y push a la rama 'english'
subprocess.run(["git", "config", "--global", "user.name", "github-actions"], check=True)
subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
subprocess.run(["git", "checkout", "-B", "english"], check=True)
subprocess.run(["rsync", "-a", "--delete", f"{temp_dir}/", "./"], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Update English translation"], check=False)
subprocess.run(["git", "push", "-u", "origin", "english", "--force"], check=True)
