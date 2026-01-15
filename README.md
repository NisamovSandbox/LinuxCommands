![Cartel Principal](.github/media/LinuxCommandsWhiteTheme.png)

[![Last commit](https://img.shields.io/github/last-commit/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff)](https://github.com/Nisamov/LinuxCommands/commits) [![License](https://img.shields.io/static/v1?label=License&message=CC%20BY-NC-SA%204.0&color=000000&style=flat-square&labelColor=ffffff)](LICENSE) [![Stars](https://img.shields.io/github/stars/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff)](https://github.com/Nisamov/LinuxCommands/stargazers) [![Forks](https://img.shields.io/github/forks/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff)](https://github.com/Nisamov/LinuxCommands/network/members)

# LinuxCommands  
### Estructura y referencia para documentar comandos y servicios en Linux

LinuxCommands nació como una recopilación de apuntes personales para organizar y entender mejor distintos comandos, scripts y servicios en Linux.

Con el tiempo, se fue estructurando para que sea más fácil de navegar y consultar, tanto para mí como para cualquier persona interesada en aprender o consultar comandos y servicios de manera práctica.

---

## Objetivos del proyecto

- Proporcionar un **formato claro y reutilizable** para documentar comandos Linux.
- Facilitar una documentación **legible para humanos y mantenible a largo plazo**.
- Reducir duplicación, ambigüedad y variaciones innecesarias entre repositorios.
- Servir como referencia práctica para administradores de sistemas, desarrolladores y equipos técnicos.

---

## Enfoque

El repositorio no pretende sustituir herramientas existentes como `man`, sino **complementarlas** mediante:

- Ficheros `commands.md` estructurados,
- Convenciones claras de documentación,
- Ejemplos prácticos y homogéneos,
- Una organización pensada para crecer sin perder consistencia.

El formato utilizado está definido formalmente en un documento de origen y se aplica de forma uniforme en todo el repositorio.

---

## Formato de documentación

El repositorio tiene su origen en el fichero [Documento de Origen](.github/origins/LinuxCommandsOrigen.md), al que posteriormente siguió una versión con una estructura más elaborada, denominado [Modelo Base](.github/origins/LinuxCommandsModel.md).

Con el crecimiento progresivo de la documentación, este enfoque resultó poco manejable debido al volumen de información concentrada en un único fichero, por lo que fue finalmente descartado.

Como solución, se adoptó un modelo estructurado y escalable de documentación, que dio lugar al uso de un índice centralizado, dando lugar al fichero [index.adoc](/document_management/index.adoc), de donde se comenzó la primera generación de PDFs

---

## Generar HTML / PDF (manualmente)

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

---

## Estructura del repositorio

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

---

## Información adicional

-  [Información general del repositorio](.github/INFO.md)

---

## Contribuciones

Las contribuciones son bienvenidas siempre que respeten el formato y la estructura definidos.  
El objetivo es mantener una documentación coherente y de alta calidad.