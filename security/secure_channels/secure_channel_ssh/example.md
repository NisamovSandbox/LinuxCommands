# Conexión SSH y Transferencia de Archivos

### Fichero de configuración
Editar fichero configuraci´ñon
```bash
nano /etc/ssh/sshd_config
```
Recargar configuración del servicio
```bash
service sshd restart
```
## Instalación del servidor SSH
En sistemas basados en Debian / Ubuntu:
```bash
sudo apt install openssh-server
```
## Conexión por SSH
Sintaxis general
```bash
ssh usuario@IP
```
Ejemplo
```bash
ssh user@192.168.115.205
```
Transferencia de archivos mediante SSH (SCP)
El comando scp permite copiar archivos de forma segura entre máquinas.
Sintaxis general
```bash
scp /ruta/origen/archivo.ext usuario@IP:/ruta/destino/archivo.ext
```
Ejemplo
```bash
scp /home/user/nombre-publica.key user@192.168.115.205:/home/user/
```
## Transferencia interactiva de archivos (SFTP)
Una vez conectado por SSH, es posible enviar archivos con:
```bash
put archivo.txt
```
Ejemplo completo
```bash
ssh user@192.168.115.205
put controller.exe
```
Configuración de FTP (vsftpd):
```bash
nano /etc/vsftpd.conf
```
Parámetros relevantes:
```ini
write_enable=YES
listen_port=3000
ftp_data_port=4000
```
Esto permite:
- Conectarse al servidor FTP por el puerto 3000
- Transferir datos por el puerto 4000
- Generación de claves con OpenSSL
- Generar clave privada cifrada
El tipo de cifrado (-aes-256-cbc) puede cambiarse.
```bash
openssl genrsa -aes-256-cbc -out nombre-privada.key 4096
```
Para ver opciones disponibles:
```bash
openssl help
```
Generar clave pública a partir de la privada
```bash
openssl rsa -in nombre-privada.key -pubout > nombre-publica.key
```
Envío de claves mediante SCP
```bash
scp /home/user/nombre-publica.key user@192.168.115.205:/home/user/
```
Desencriptado con clave privada
```bash
openssl rsautl --decrypt -inkey claveprivada.key -in encriptado.enc > desencriptado
```