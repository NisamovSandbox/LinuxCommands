![Cartel Principal](.github/media/LinuxCommandsWhiteTheme.png)

[![Last commit](https://img.shields.io/github/last-commit/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff)](https://github.com/Nisamov/LinuxCommands/commits) [![License](https://img.shields.io/static/v1?label=License&message=MIT&color=000000&style=flat-square&labelColor=ffffff)](LICENSE) [![Stars](https://img.shields.io/github/stars/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff)](https://github.com/Nisamov/LinuxCommands/stargazers) [![Forks](https://img.shields.io/github/forks/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff)](https://github.com/Nisamov/LinuxCommands/network/members)

# LinuxCommands  
### Estructura y referencia para documentar comandos y servicios en Linux

LinuxCommands nació como una recopilación de apuntes personales para organizar y entender mejor distintos comandos, scripts y servicios en Linux.

Con el tiempo, se fue estructurando para que sea más fácil de navegar y consultar, tanto para mí como para cualquier persona interesada en aprender o consultar comandos y servicios de manera práctica.

---
<details open>
<summary><strong>• OBJETIVOS DEL PORYECTO</strong></summary>
<h1>Objetivos del proyecto</h1>

- Proporcionar un **formato claro y reutilizable** para documentar comandos Linux.
- Facilitar una documentación **legible para humanos y mantenible a largo plazo**.
- Reducir duplicación, ambigüedad y variaciones innecesarias entre repositorios.
- Servir como referencia práctica para administradores de sistemas, desarrolladores y equipos técnicos.
</details>

---
<details open>
<summary><strong>• ENFOQUE DEL PORYECTO</strong></summary>
<h1>Enfoque del proyecto</h1>

El repositorio no pretende sustituir herramientas existentes como `man`, sino **complementarlas** mediante:

- Ficheros `commands.md` estructurados,
- Convenciones claras de documentación,
- Ejemplos prácticos y homogéneos,
- Una organización pensada para crecer sin perder consistencia.
</details>

---
<details close>
<summary><strong>• GENERACIÓN MANUAL DE DOCUMENTOS</strong></summary>
<h1>Generación manual de documentos</h1>

Instrucciones rápidas para generar la documentación localmente y comprobar la jerarquía y el índice.

Prerequisitos:
- `asciidoctor` para HTML.
- `asciidoctor-pdf` para generar PDF directamente (opcional).

Instalación (si dispone de Ruby/gems):
```bash
gem install asciidoctor
gem install asciidoctor-pdf
```
Generar HTML:
```bash
asciidoctor -b html5 document_management/index.adoc -o document_management/index.html
```
Generar PDF (directo con `asciidoctor-pdf`):
```bash
asciidoctor-pdf document_management/index.adoc -o document_management/LinuxCommands.pdf
```
</details>

---
<details close>
<summary><strong>• ESTRUCTURA DEL PROYECTO</strong></summary>
<h1>Estructura del proyecto</h1>

La organización del repositorio está pensada para facilitar la navegación y el crecimiento progresivo del contenido:

<!-- AUTO-GENERATED-INDEX:START -->
- [document_management](/document_management)
- [fundamentals](/fundamentals)
- [networking](/networking)
- [permission_management](/permission_management)
- [process_tasks](/process_tasks)
- [scripting](/scripting)
- [security](/security)
- [services](/services)
- [software_management](/software_management)
- [storage](/storage)
- [system_data](/system_data)
- [user_permissions](/user_permissions)
- [web_server](/web_server)
<!-- AUTO-GENERATED-INDEX:END -->
</details>

---
<details close>
<summary><strong>• FORMATO DE DOCUMENTACIÓN</strong></summary>
<h1>Formato de documentación</h1>

El repositorio sigue un estándar fijo de documentación para mantener el orden y permitir una correcta indexación a la hora de generar PDFs.

Premodelos de ejemplo:
- [Ejemplo de premodelo en Markdown (.md)](.github/templates/markdown.md)
- [Ejemplo de premodelo en LaTeX (.tex)](.github/templates/latex.tex)
- [Ejemplo de premodelo en Documento Ascii (.adoc)](.github/templates/asciidocument.adoc)

Se pide tener en cuenta el [PULL_REQUEST_TEMPLATE](.github/PULL_REQUEST_TEMPLATE) en caso de querer colaborar con el repositorio.
</details>

---
<details close>
<summary><strong>• CONTRIBUYE AL PROYECTO</strong></summary>
<h1>Contribuye al proyecto</h1>

Las contribuciones son bienvenidas siempre que respeten el formato y la estructura definidos.  
El objetivo es mantener una documentación coherente y de alta calidad.

> [Crear pull request](https://github.com/Nisamov/LinuxCommands/pulls)
</details>

---
<div align="center">
  <p>Linux Commands - By Nisamov | MIT License - 2026</p>
  <p>Contacto: <a href="mailto:nisamov.contact@gmail.com">nisamov.contact@gmail.com</a></p>
</div>