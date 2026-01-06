# Teoría: Gestión de Ficheros y Directorios en Linux
## Sintaxis de comandos
Los comandos en sistemas GNU/Linux siguen una sintaxis general:
```
comando [opciones] [argumentos]
```
- Comando: programa que se ejecuta.
- Opciones (o flags): modifican el comportamiento del comando.
- Argumentos: indican sobre qué elementos actúa el comando (archivos, directorios o rutas).
No todos los comandos requieren opciones ni argumentos.
## Modificación de metadatos
En Linux, los ficheros disponen de metadatos almacenados en el inodo (permisos, propietario, fechas, etc.).
### El comando `touch`
El comando `touch` tiene como función principal modificar los metadatos temporales de un fichero:
- atime: último acceso
- mtime: última modificación del contenido
Si el fichero no existe, `touch` lo crea como efecto secundario.
#### Sintaxis
```bash
touch [ruta/]nombre_fichero
```
#### Ejemplos
Crear un fichero (si no existe):
```bash
touch file.txt
```
Actualizar las fechas de un fichero existente:
```bash
touch file.txt
```
Crear un fichero en una ruta concreta:
```bash
touch /home/user/Documents/file.txt
```
Asignar una fecha concreta:
```bash
touch -t 202601062130 file.txt
```
Copiar las marcas de tiempo de otro fichero:
```bash
touch -r origen.txt destino.txt
```
> En Linux, la extensión de un fichero no determina su función. El sistema solo distingue entre ficheros y directorios.
### Ficheros ocultos
Un fichero se considera oculto si su nombre comienza por un punto (`.`):
```bash
touch .hidden
```
Estos ficheros no se muestran por defecto y requieren opciones específicas para ser listados.
## Listado de contenido
### El comando `ls`
El comando `ls` permite listar el contenido de un directorio.
#### Sintaxis
```bash
ls [opciones] [ruta]
```
#### Opciones comunes
- `-l` listado detallado
- `-a` muestra ficheros ocultos
- `-R` listado recursivo
- `-r` invierte el orden del listado
- `-h` tamaños en formato legible
### Comodines del shell
Los comodines no son opciones de `ls`, sino del shell:
- `*` > cualquier cadena de caracteres
- `?` > un solo carácter
Ejemplos:
```bash
ls *.txt
ls file?.sh
```
> Nota: `ll` no es un comando estándar, sino un alias de `ls -l` presente en algunas distribuciones.
### Salida de `ls -l`
Ejemplo:
```
-rwxr--r-- 1 root root 56 Jan 24 20:51 bucle.sh
```
Estructura:
```
[permisos] [nº enlaces] [propietario] [grupo] [tamaño] [fecha modificación] [nombre]
```
## Estructura en árbol
### El comando `tree`
El comando `tree` muestra la estructura de directorios en forma jerárquica.
Instalación:
```bash
sudo apt install tree
```
Opciones comunes:
- `-d` > solo directorios
- `-f` > ruta completa
- `-a` > incluye ocultos
- `-u` > usuario propietario
- `-g` > grupo propietario
- `-h` > tamaño legible
## Enlaces
### El comando `ln`
Permite crear enlaces entre archivos o directorios.
#### Enlaces duros
```bash
ln archivo_original enlace_duro
```
Características:
- Comparten el mismo inodo
- No son copias
- No se pueden crear sobre directorios
- No atraviesan sistemas de archivos
- El contenido persiste mientras exista al menos un enlace
#### Enlaces simbólicos
```bash
ln -s archivo_original enlace_simbolico
```
Características:
- Tienen su propio inodo
- Apuntan a una ruta
- Pueden enlazar directorios
- Pueden cruzar sistemas de archivos
- Se rompen si el destino desaparece

Eliminar un enlace simbólico:
```bash
unlink enlace_simbolico
```
Para más información:
```bash
man ln
```