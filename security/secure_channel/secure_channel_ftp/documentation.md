# FTP Secure Channel (SSH / SFTP)
## Topología y equipos

Máquinas implicadas:
- Equipo 1 (Emisor): 192.168.115.204
- Equipo 2 (Receptor): 192.168.115.205

La comunicación se realiza mediante SFTP sobre SSH, garantizando confidencialidad e integridad del canal.
El cifrado de los archivos se refuerza mediante GPG.

## Instalación de dependencias
```sh
sudo apt update
sudo apt install openssh-server vsftpd gpg ufw
```
Descripción de los paquetes instalados:
- openssh-server: Permite conexiones remotas seguras mediante SSH y SFTP.
- vsftpd: Servidor FTP (en este escenario se documenta, aunque el canal seguro se basa en SFTP).
- gpg: Herramienta de cifrado y firma de archivos.
- ufw: Cortafuegos para la gestión de reglas de red.

El servicio que gestiona las conexiones SSH es **sshd**.

## Configuración del servidor FTP (vsftpd)
Acceso al fichero de configuración:
```sh
sudo nano /etc/vsftpd.conf
```
Verificar el puerto de escucha: `listen_port=22`

> Nota:
> El puerto 22 es el estándar de SSH/SFTP. Puede modificarse según las políticas de seguridad o el entorno de red, siempre asegurando que el cortafuegos permita dicho puerto.

Guardar los cambios y cerrar el editor.

## Reinicio y verificación del servicio SSH
Reiniciar el servicio para aplicar cambios:
```sh
sudo service ssh restart
```
Comprobar el estado:
```sh
sudo systemctl status ssh
```
## Configuración del cortafuegos (UFW)
Permitir conexiones SSH/SFTP:
```sh
sudo ufw allow 22/tcp
sudo ufw enable
sudo ufw status
```
## Gestión de claves GPG
Ver claves existentes
```sh
gpg -k
```
Generar una nueva clave GPG (modo guiado)
```sh
gpg --gen-key
```
Generación avanzada (selección de algoritmo y tamaño de clave)
```sh
gpg --full-generate-key
```
Permite definir:
- Tipo de cifrado (RSA, ECC, etc.)
- Número de bits
- Fecha de expiración
- Identidad asociada (nombre y correo)
## Cifrado de archivos con GPG
Cifrado simétrico en ASCII (armour):
```sh
gpg --symmetric -a ejercicio.txt
```
Cifrado simétrico en binario:
```sh
gpg --symmetric ejercicio.txt
```
Especificando algoritmo (Twofish o 3DES):
```sh
gpg --symmetric --cipher-algo twofish ejercicio.txt
gpg --symmetric --cipher-algo 3des ejercicio.txt
```
Cifrado asimétrico (clave pública)
Encriptar un archivo para un destinatario concreto:
```sh
gpg --encrypt --recipient email@dominio.com archivo.ext
```
## Exportación e importación de claves
Exportar clave pública en ASCII
```sh
gpg --export -a email@dominio.com > nombre.key.asc
```
Exportar clave pública en binario
```sh
gpg --export email@dominio.com > nombre.key
```
Importar una clave pública
```sh
gpg --import nombre.key.asc
```
## Descifrado de archivos
Descifrar un archivo:
```sh
gpg -d archivo.gpg
```
Guardar el resultado en un fichero concreto:
```sh
gpg -d archivo.gpg > archivo_descifrado.txt
```
## Transferencia segura de archivos (SFTP)
Establecer conexión con el equipo receptor
```sh
sftp usuario@192.168.115.205
```
Comandos básicos en sesión SFTP
Enviar archivo al equipo:
```sh
put archivo.gpg
```
Descargar archivo:
```sh
get archivo.gpg
```
Salir de la conexión:
```sh
exit
```