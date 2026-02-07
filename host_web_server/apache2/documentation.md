# Documentación Apache2
<!--Documentado por Andrés Ruslan Abadías Otal (Nisamov)-->

## Instalación
Para evitar posibles problemas durante la instalación, se recomienda actualizar los paquetes del sistema.
```sh
# Esto es unicamente opcional
sudo apt update && sudo apt upgrade -y
```

Instalación de apache2:
Instalar el servicio con los privilegios de administrador.
```bash
sudo apt install apache2
```

## Creación de la página
Para crear una página hay que dirigirse a la dirección `/var/www/`, donde se observará un fichero llamado `index.html`.
Crear un directorio dentro de la ubicación anterior con el nombre del dominio (por organización) que queramos, este tiene que acabar en un prefijo `.es, .org, .com`...
Posteriormente acceder al interior del directorio creado y ahi dentro crear un fichero llamado `index.html`.
```bash
#Posicionamiento en la ubicación mencionada
cd /var/www/

#Crear el directorio con el prefijo
mkdir mipagina.es

#Acceder al directorio
cd mipagina.es

#Crear el fichero dentro del directorio creado
touch index.html
```

## Edición de la página
Para dar estructura a la página, es necesario editar el fichero `index.html` creado anteriormente.
Si se quiere agregar diseño y funcionalidad, es requerido usar ficheros `.css` y `.js`.
```bash
#Editar el fichero index.html
sudo nano index.html
```

Dentro del fichero `index.html` agregar la estructura básica de HTML5:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MiPagina</title>
    <!--Elimina la siguiente linea si no quieres aplicar estilos-->
    <link href="styles/style.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <!--Agregar el contenido que veas necesario-->
    <p>Este es el contenido de tu pagina</p>
    <u>He seguido la guia de github.com/Nisamov</u>
    <!--Eliminar la siguiente linea si no quieres aplicar estilos-->
    <script src="scripts/script.js"></script>
</body>
</html>
```
Para poner un ejemplo de como sería la estructura con la implementación de estilos y scripts hay que tener en cuenta que estos ficheros se deberian agregar en subdirectorios dentro de la ruta de la pagina principal.
Esto permitira una buena organizacion, en el siguiente ejemplo se presenta la estructura ideal para este proceso.

## Estructura de directorio
```
var
└── www
    └── mipagina.es
        ├── index.html
        ├── styles
        │   └── style.css
        └── scripts
            └── script.js
```

Para crear esta misma estructura hay que estar dentro de la ruta de la pagina principal `mipagina.es` y crear dos directorios, el primero seria `styles`, donde almacenar los ficheros de estilos `.css` y el segundo `scripts`, donde se ubicarán los mismos `.js`.

Para llevar a cabo este proceso opcional, hay que hace lo siguiente:
```bash
#Posicionamiento en la ruta
cd /var/www/mipagina.es

#Crear dos directorios
mkdir styles scripts
```
## Estilo y Funcionamiento de la pagina con CSS y JS

Tras la creacion de los directorios, se crearán ficheros con el codigo necesario, el cual será interpretado por la pagina principal `index.html`.
Para crear estos ficheros es necesario acceder a cada directorio y crear un fichero con su correspondiente contenido:
```bash
#Posicionamiento dentro de la ruta JavaScript (scripts)
cd /var/www/mipagina.es/scripts

#Crear y editar el primer fichero de scripts
nano script.js
```

Tras crear el fichero dentro de la ruta especificada, ingresaremos el código, este mismo estara vinculado a la pagina principal (debido al nombre y ruta usados, estos mismos estan referenciados en la pagina web, por lo que si se quiere, se puede cambiar la ruta de la pagina, no obstante, para su correcto funcionamiento es recomendable usar una ruta clara y estática.

El codigo del fichero JavaScript puede ser el que se desee, en este caso se usara un codigo simple como muestra de correcto funcionamiento:
```js
//Alerta que muestra el correcto funcionamiento del codigo
alert("El Codigo JavaScript Funciona correctamente");
//Mensaje por consola indicando el correcto funcionamiento del mismo
console.log("Correcto funcionamiento");
```

Para poder aplicar estilos en la pagina, es necesario usar el mismo sistema usado durante la creacion de scripts de `JavaScript`, para esto, hay que ubicarse en la ruta de los estilos creada anteriormente y crear un fichero donde almacenaremos el codigo de los estilos de la apgina principal, este fichero debera contener el nombre referenciado en la pagina web, el cual es `style.css`, para que pueda funcionar, asi como el codigo `.js` debera estar en la misma ruta que la mencionada en la pagina web (/var/www/mipagina.es/styles).
```bash
#Posicionamiento en la ruta de los estilos (styles)
cd /var/www/mipagina.es/styles

#Crear un fichero el cual almacenara los estilos de la pagina
nano style.css
```

Posteriormente agregar contenido dentro del fichero, este ha de ser código `CSS`, esto permitira a la pagina obtener un estilo, bien sea un color de fondo, efectos, fuentes de texto...

Un ejemplo sencillo de codigo `CSS` es el siguiente:
```css
/*Color de fondo en el cuerpo de la pagina*/
body {
  background-color: #fefbd8;
}

/*Color de fondo en los titulos h1*/
h1 {
  background-color: #80ced6;
}

/*Estilos cuerpo de texto*/
p {
font-family: 'Open Sans';
font-size: 14px;
color: #ccc;
line-height: 18px;
margin-bottom: 20px;
}
```
Tras esto, se crea un certificado, permitiendo que la página funcione con `https`, para ello es necesario instalar `openssl`:
```bash
sudo apt install openssl
```
A continuación habilitar el modo `ssl`:
```bash
sudo a2enmod ssl
```
Finalmente reiniciar el servicio apache2:
```bash
sudo systemctl restart apache2
```

Acceder a la localización de directorios y ficheros de configuración, copiar el fichero `000-default.conf`, renombrándolo como `mipagina.es.conf`.
```bash
#Acceder a la ruta donde se almacena la configuración de las páginas dentro de apache
cd /etc/apache2/sites-available

#Clonar el fichero 000-default.conf y lo renombramos con el nombre de la pagina, seguido de un ".conf"
sudo cp 000-default.conf mipagina.es.conf
```
Tras hacer una clonación, acceder al interior de la copia creada por nosotros con el nombre de la pagina, a la cual le aplicaremos atributos para lograr que la pagina funcione.

Acceder con permisos de superusuario y agregar el siguiente contenido sustituyendo todo lo que pueda haber en su interior:
```bash
#Editar el contenido como root
sudo nano mipagina.es.conf
```

Dentro del  fichero agregar el siguiente contenido:
```bash
<VirtualHost *:80>
ServerAdmin webmaster@localhost
DocumentRoot /var/www/mipagina.es
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog /etc/apache2/sites-available/access.log
ServerName www.mipagina.es
</VirtualHost>

<VirtualHost *:443>
ServerName mipagina.es
Redirect / http://www.mipagina.es
</VirtualHost>

# Contenido para certificado SSL
<VirtualHost *:443>
ServerName www.mipagina.es
DocumentRoot /var/www/mipagina.es
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog /etc/apache2/sites-available/access.log
SSLEngine on
SSLCertificateFile /etc/apache2/certificate/apache-certificate/apache-certificate.crt
SSLCertificateKeyFile /etc/apache2/certificate/apache.key
</VirtualHost>
```
Esto permitira enlazar la configuracion y redireccion mediante http a nuestra pagina creada previamente, en caso de haber utilizado un nombre diferente, se debe sutituir cada valor que hace referencia a `mipagina.es` con el nombre que sea requerido.

Aplicar los cambios de la configuración establecida dentor de la ruta `/etc/apache2/sites-available`:
```bash
#Activar nuestra carpeta, agregando a2ensite + nombreDeCarpeta
sudo a2ensite mipagina.es
```

Tras seguir todos los pasos previos, hay que asignar una direccion a la pagina, para ello hay que editar el fichero `/etc/hosts`:
```bash
#Editar el fichero /etc/hosts
sudo nano /etc/hosts
```
En el interior de este asignar una ip al fichero index de la pagina.

La direccion 127.0.1.1 está asociada a la propia maquina, mientras que la ip `40.0.0.2` es una direccion asociada a `mipagina.es`, es una direccion pública.
```bash
127.0.0.1       localhost
127.0.1.1       nisamov
40.0.0.2        mipagina.es        www.mipagina.es
# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```
Configuración de puertos en `/etc/apache2/ports.conf`, accediendo como root:
```bash
#Editar el fichero de configuracion de puertos de apache2
sudo nano /etc/apache2/ports.conf
```
En el interior agregar el siguiente contenido, permitiendo la escucha por los puertos 80 y 443:
```bash
Listen 80
#Configuracion adicional para el certificado ssl con escucha por el puerto 443
<IfModule ssl_module>
        Listen 443
</IfModule>

<IfModule mod_gnutls.c>
        Listen 443
</IfModule>
```

Reiniciar el servicio apache2:
```bash
sudo systemctl restart apache2
```

Acceder a la configuración de apache2:
```bash
sudo nano /etc/apache2/apache2.conf
```
Agregar el siguiente contenido en las últimas lineas de la configuración, permitiendo sobreescribir las directivas anteriores, siendo este un paso necesario para el HTTPS y su funcionamiento:
```bash
<Directory /var/www/mipagina.es>
AllowOverride All
</Directory>
```

Crear varios directorios para almacenar los certificados y claves para la pagina:
```bash
#Acceder a la ruta donde almacenar los certificados
cd /etc/apache2/sites-available
```

```bash
#Crear el primer directorio de almacenamiento, con el nombre "certificado"
mkdir certificado
#Acceder al interior del directorio creado previamente
cd certificado
#En el siguiente comando se crea un certificado con el nombre "apache-certificado.crt"
#Creación de una llave llamada "apache.key", la cuales se usarán en la configuracion previa, dentro de /etc/apache2/sites-available/mipagina.es.conf
sudo openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out apache-certificado.crt -keyout apache.key
```
Tras la creacion del certificado y la llave solicitará el ingreso de datos, siendo el unico requerido `Common name`, donde deberemos escribir la direccion ip `fija`.

Estas llaves y certificados son necesarios dentro de la configuración previa "/etc/apache2/sites-available/mipagina.es.conf", haciendo referencia a estos mismos, los cuales usará para la conexión HTTPs.

Reiniciar el servicio apache2:
```sh
sudo service apache2 restart
```
Si se intenta acceder a la pagina, mostrará un aviso "Advertencia: Riesgo potencial de seguridad a continuación", para evitar un aviso similar hay que acceder al a configuración de la página:
```sh
sudo nano /etc/apache2/sites-available/mipagina.es.conf
```
Agregar la siguiente linea:
`Redirect permanent / http://www.mipagina.es`, redirigiendo todas los accesos http, a una conexión segura mediante https:
```sh
<VirtualHost *:80>
ServerAdmin webmaster@localhost
DocumentRoot /var/www/mipagina.es
Redirect permanent / http://www.mipagina.es # Ubicación de la linea mencionada
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog /etc/apache2/sites-available/access.log
ServerName www.mipagina.es
</VirtualHost>

<VirtualHost *:443>
ServerName mipagina.es
Redirect / http://www.mipagina.es
</VirtualHost>

<VirtualHost *:443>
ServerName www.mipagina.es
DocumentRoot /var/www/mipagina.es
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog /etc/apache2/sites-available/access.log
SSLEngine on
SSLCertificateFile /etc/apache2/certificate/apache-certificate/apache-certificate.crt
SSLCertificateKeyFile /etc/apache2/certificate/apache.key
</VirtualHost>
```
Reiniciar el servicio apache2:
```bash
sudo service apache2 restart
```
Si se ha seguido el procedimiento indicado, la página debería ser funcional, durante la aplicación de cambios y los reinicios de apache2 pueden surgir errores, los cuales son detallados durante la misma ejecución.