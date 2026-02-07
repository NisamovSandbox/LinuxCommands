# Documentación NGINX
<!--Documentado por Andrés Ruslan Abadías Otal (Nisamov)-->

Instalar los servicios necesarios para poder continuar:
```bash
sudo apt install nginx
```
Posteriormente acceder al fichero de configuración de red y establecer una ip fija en el equipo.

Acceder a la ruta `/var/www` y crear un directorio en su interior:
```bash
#Acceder a la ruta
cd /var/www
#Crear un directorio en su interior
mkdir mipagina.es
#Otorgar permisos
sudo chmod 755 mipagina.es
#Acceder al directorio creado
cd mipagina.es
#Crear un index.html, que será la página principal
nano index.html
```
Tras crear y abrir el fichero `index.html`, agregar la estructura basica de una página web:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    	<meta charset="UTF-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<title>Mi Página</title>
</head>
	<body>
    	<p>Contenido cuerpo de página</p>
	</body>
</html>
```
En internet, acceder a https://www.duckdns.org y registrarse.

Una vez registrado, crear un subdominio (por ejemplo `mipagina.duckdns.org`) y asociarlo a la IP pública del equipo.

DuckDNS se encarga de la resolución DNS automáticamente, por lo que no es necesario modificar el fichero `/etc/hosts`.

Tras la propagación DNS, el dominio será accesible desde cualquier dispositivo con conexión a Internet.

Acceder a la ruta de nginx `/etc/nginx/sites-available` y crear el fichero de configuración:
```bash
#Acceder a la ruta
cd /etc/nginx/sites-available
#Copiar el fichero y lo renombramos como mipagina
sudo cp default mipagina.es
#Editar el fichero
sudo nano mipagina.es
```
Dentro del fichero previo, agregar el siguiente contenido:
```nginx
server {
listen 80;
root /var/www/mipagina.es;
index index.html index.htm;
#Aquí hacer referencia a la direccion con la que se vinculará dentro de duckDNS
server_name mipagina.duckdns.org www.mipagina.duckdns.org;
location / {
try_files $uri $uri/ =404;
}
}
```
Posteriormente hacer un enlace simbólico
```bash
sudo ln -s /etc/nginx/sites-available/mipagina.es /etc/nginx/sites-enabled/mipagina.es 
```
Reiniciar el servicio nginx:
```bash
#Reiniciar el servicio
service nginx restart
#Comprobar su estado
service nginx status
```
Para comprobar su correcto funcionamiento, buscar la página con el enlace que se haya creado, dependiendo de la direccion registrada variará este mismo:
```bash
#Realizar las busquedas de la pagina en internet
mipagina.es.duckdns.org
www.mipagina.es.duckdns.org
```
Para continuar con la página, instalaremos más servicios, en este caso será openssl:
```bash
#Instalar el servicio openssl
sudo apt install openssl
```
Acceder a la ruta `/etc/nginx` y crear un directorio donde almacenar las claves:
```bash
#Acceder a la ruta previa
cd /etc/nginx
#Crear un directorio
mkdir ssl
#Otorgar permisos al directorio previo
chmod 700 ssl
```
Creación de claves:
```bash
#Crear las claves y solicitud dentro de /etc/nginx/ssl
openssl genrsa -out /etc/nginx/ssl/clave_privada.key 4096
openssl req -new -key /etc/nginx/ssl/clave_privada.key -out /etc/nginx/ssl/solicitud.csr
#Acceder a la ruta ssl y comprobar el resultado
cd ssl
#Comprobación de la creación de “clave_privada.key” y “solicitud.csr”
ls -al
#Generar un certificado dentro del mismo directorio
openssl x509 -req -days 365  -in /etc/nginx/ssl/solicitud.csr -signkey /etc/nginx/ssl/clave_privada.key -out /etc/nginx/ssl/certificado.crt
#Comprobación de la creación de “certificado.crt”
ls -al
```
Posteriormente acceder a la ruta `/etc/nginx/sites-enabled/mipagina.es`
```bash
sudo nano /etc/nginx/sites-enabled/mipagina.es
```
Dentro de esta ruta agregaremos el siguiente contenido:
```nginx
server {
listen 80;
root /var/www/mipagina.es;
index index.html index.htm;
server_name mipagina.duckdns.org www.mipagina.duckdns.org;
location / {
try_files $uri $uri/ =404;
}
}

server {
listen 443 ssl;
server_name mipagina.duckdns.org www.mipagina.duckdns.org;
root /var/www/mipagina.es;
index index.html index.htm;
ssl_certificate /etc/nginx/ssl/certificado.crt;
ssl_certificate_key /etc/nginx/ssl/clave_privada.key;
location / {
try_files $uri $uri/ =404;
}
}
```
Este contenido permite establecer conexión con la dirección `duckdns`, así como especificaremos la ruta de los ficheros, siendo estos los certificados y claves requeridas para una conexión segura.

Por último reiniciar los siguiente servicios y si el procedimiento se ha llevado a cabo correctamente, la página estará lista para ser vista desde cualquier dispositivo.
```bash
#Reiniciar todos las herramientas
service nginx restart
#Comprobar el estado de las mismas
service nginx status
```