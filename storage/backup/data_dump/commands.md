Descripción:
Le indicas un archivo de origen y uno de destino, si no tiene destino, lo crea.
Del archivo origen -> pregunta cuántos quieres copiar al archivo destino.
Usado comúnmente para crear o llenar archivos o crear contraseñas de forma aleatoria.

Etimología: dd = Data Definition: Comando para añadir los datos que luego debían ejecutarse.

Estructura:
- `InputFile; OutputFile; Blocks`

Uso: `dd if=ArchivoOrigen of=ArchivoDestino.extensión bs=BloquesACopiar`
Si le pido acceder al dispositivo /dev/zero y le pido que me de X número de sectores, rellena con null
Si no se indica el número de bytes copiados, se rellena a más no poder.

> Recuperación de S.O con rescatux

```sh
# Genera un archivo fich.txt con 999999bits tipo null
dd if=/dev/null of=fich.txt bs=999999
```
```sh
# Genera un archivo fich.txt con 999999bits aleatorios
dd if=/dev/random of=fich.txt bs=999999
```
```diff
# Llena hasta el límite la primera partición del primer disco
- Peligro, una vez realizada esta acción, el disco quedaría inutilizable
dd if=/dev/random of=/dev/sda1
# Debiado a esta capacidad para destrozar discos, el comando dd, fué conocido también como "Disk Destroyer"
```
```sh
# Creacion de fichero binario con 20bits tipo zero
dd if=/dev/zero of=archivo_29MB.bin bs=1M count=20
```