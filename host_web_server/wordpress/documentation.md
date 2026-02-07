# Documentación Wordpress
<!--Documentado por Andrés Ruslan Abadías Otal (Nisamov)-->

Actualizar los paquetes de la máquina:
```bash
sudo apt upgrade && sudo apt update -y
```
Instalar las dependencias y paquetería de los programas necesarios:
```bash
sudo apt install apache2 php8.1 php8.1-bcmath php8.1-curl php8.1-gd php8.1-mbstring php8.1-mysql php8.1-pgsql php8.1-xml php8.1-zip mariadb-server mariadb-client wget
```
O instalación individual:
```bash
sudo apt install apache2
sudo apt install php7.4
sudo apt install wget
sudo apt install mariadb-server
sudo apt install mariadb-client
sudo apt install php8.1
sudo apt install php8.1-mysql
sudo apt install php8.1-curl
sudo apt install php8.1-gd
sudo apt install php8.1-bcmath
sudo apt install php8.1-cgi
sudo apt install php8.1-ldap
sudo apt install php8.1-mbstring
sudo apt install php8.1-xml
sudo apt install php8.1-soap
sudo apt install php8.1-xsl
sudo apt install php8.1-zip
#En caso de ser necesario, instalar:
sudo apt install libapache2-mod-php php-mysql -y
```
Este comando permitirá instalar todos los paquetes en un solo comando, evitando tener que ir por fragmentos, ahorrando tiempo.

Usando el entorno gráfico instalar wordpress y descompresión del mismo,
Mover el directorio a la ruta raíz.
```bash
sudo mv wordpress /wordpress
```
Otorgar permisos a los directorios con los que se va a trabajar:
```bash
cd /wordpress
#Otorgar permisos dentro del repositorio
sudo chown www-data:www-data .
sudo chown www-data:www-data -R *
```
Deshabilitar el fichero de configuración de apache2:
```bash
#Acceder a la ruta /sites-available
cd /etc/apache2/sites-available
#Deshabilitar la configuración por defecto
sudo a2dissite 000-default
```
Reiniciar el servicio apache para comprobar los cambios:
```bash
#Reiniciar el servicios apache2
sudo service apache2 restart
```
Crear un nuevo fichero de configuración en la ruta `/etc/apache2/sites-available/`:
```bash
#Crear el fichero de configuración y edición del mismo
sudo nano wordpress.conf
```
Agregar el contenido de la configuración con las rutas necesarias para su funcionamiento:
```bash
#Ubicación actual: /etc/apache2/sites-available/wordpress.conf
<VirtualHost *:80>
  ServerAdmin webmaster@localhost
  DocumentRoot /wordpress
  <Directory /wordpress>
  DirectoryIndex index.php
  AllowOverride All
  Require all granted
  </Directory>
  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Habilitar la página:
```bash
#Habilitar la pagina wordpress
sudo a2ensite wordpress
```
Reiniciar el servicio apache2:
```bash
#Reniciar el servicio apache2
sudo systemctl restart apache2
```
Crear las bases de datos para la página, comenzando con la ejecucion del gestor de bases de datos:
```sql
#Ejecución del gestor de bases de datos
sudo mysql -u root -p
```
Modificar la información del usuario root:
```sql
update mysql.user set plugin=’mysql_native_password’ WHERE user=’root’;
```
Leer la lista de privilegios:
```sql
flush privileges;
```
Creación de una base de datos para la página:
```sql
create database wordpress;
exit;
```
Ajustar parámetros básicos de seguridad mediante la instalación segura:
```bash
sudo mysql_secure_installation
```
Durante la instalación, realizará varias preguntas, ae stas contestamos que sí, en la última pregunta, `solicitará una contraseña`, esta misma será para `mysql`, **guarda esa contraseña en un papel o un documento de forma que no la pierdas**.

Tras el proceso comleto es posible que pida crear una base de datos `wp-config.php`, en el interior de esta base de datos es necesario agregar la siguiente estructura:
```php
<?php
// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );
/** Database username */
define( 'DB_USER', 'root' );
/** Database password */
define( 'DB_PASSWORD', 'andres' );
/** Database hostname */
define( 'DB_HOST', 'localhost' );
/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );
/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );
define( 'AUTH_KEY',         ']&eKuM6^mw^;,|:[-p?_[XJBkMr<E8&cJGR(.k|1v%bl-Q7szq|ipsgb411e4U}G' );
define( 'SECURE_AUTH_KEY',  '7|6f^<J>F?4RR%}%k(IY;s)cqY%M4cW*Yp?qXroB[(jf9Zwfzx|r$G{$J3r86qf<' );
define( 'LOGGED_IN_KEY',    ')xhXtUA|AkftoP@R-dPm|iI{?!i7^T>s~/*(@{,naV#9i kZ1pCK]|(31K5}u*J7' );
define( 'NONCE_KEY',        '4$pu@PCrf|dBg^4K_Q>Iqaf| 5St~GU,n<#nl`2PghIU G55z/N]lcl%l68kfHd-' );
define( 'AUTH_SALT',        'MD.SxW+}g`q3Ub}LN>!|,P<+Ya5QFR(vd1H2kE&U(|cl-hGUPq<I${#Ahaxl*H4J' );
define( 'SECURE_AUTH_SALT', 'E^p{[?C4}/0ZG:}7V)OBakc~cL]M=}X.=:12sq `XM|O+]3](54sZZamq9g&/woy' );
define( 'LOGGED_IN_SALT',   '4@p34O)[p)X}N KVsWu_l5<oaXRH>U/{XR,?d8;vRyI=,(Z8vNy%}yG$uH8)ht|9' );
define( 'NONCE_SALT',       'a2u!6q:UrqN96JM,tWy-W==Z&[:!&0pNrbiC{XQ0DdG%! ip^N<F1&M0 Gx|AsE(' );
/**#@-*/
$table_prefix = 'wp_';
define( 'WP_DEBUG', false );
/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}
/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
```
Tras llevar a cabo todas las configuraciones necesarias, acceder al navegador en la ruta de la página, donde completar todo el proceso de setup.