import sys
import re
from pathlib import Path

errors = []

# Recorrer todos los index.adoc cambiados
for filepath in sys.argv[1:]:
    path = Path(filepath)
    content = path.read_text(encoding='utf-8')
    # 1Revisar título principal
    if not content.startswith("="):
        errors.append(f"{filepath}: El título principal debe empezar con '='")
    # Revisar que no haya títulos mayores a nivel 2
    if re.search(r"^===+", content, re.MULTILINE):
        errors.append(f"{filepath}: No se permiten títulos con más de dos '='")
    # Revisar includes
    for include in re.findall(r"include::(.*?)\[\]", content):
        if not include.endswith(".adoc"):
            errors.append(f"{filepath}: include mal formado -> {include}")
if errors:
    print("\n".join(errors))
    sys.exit(1)

sys.exit(0)
