```sh
#----------------------------------#------------------------------------------------------------------------------------------------#
| COMANDO                          | DESCRIPCIÓN                                                                                    |
#----------------------------------#------------------------------------------------------------------------------------------------#
├── rsync                          §; Herramienta para sincronizar y copiar archivos y directorios de forma eficiente.
│   ├── -a                         §; Modo archivo (preserva permisos, propietarios, enlaces simbólicos, fechas, etc.).
│   ├── -v                         §; Verboso, muestra el progreso de la copia.
│   ├── -h                         §; Tamaños legibles (human-readable, ej. MB, GB).
│   ├── -z                         §; Comprime los datos durante la transferencia (útil para redes lentas).
│   ├── --exclude='PATTERN'        §; Excluye archivos o directorios que coincidan con el patrón.
│   ├── -r                         §; Copia directorios de manera recursiva (ya incluido en `-a`).
│   ├── -u                         §; Solo copia archivos más nuevos que los existentes en destino.
│   ├── -n                         §; Realiza una prueba sin hacerla, similar a (--dry-run)
│   ├── --progress                 §; Muestra el progreso de la transferencia archivo por archivo.
│   └── /origen /destino           §; Especifica la ruta de origen y destino de la copia.
```

rsync `[optional modifiers] [Origen] [Destino]`
Transfiere y sincroniza archivos o directorios de manera eficiente entre una máquina local o un servidor remoto.

`rsync -r original/ duplicate/` Copiar directorios = rsync {dirección de origen} {dirección de destino}
`apt install shhpass` Instala el servicio sshpass
`apt install cron` Instala el servicio crontab para la automatización

Acceder a shell remoto
```sh
rsync –exclude={que excluir} –delete .arvPn examen/ prueba2/ (elimina todo menos que los que se excluyen y los copia dentro de prueba2 de /examen)
```