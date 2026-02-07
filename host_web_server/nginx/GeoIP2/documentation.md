# Módulo GeoIP2

Módulo complementario de la guía [web nginx](/web_server/nginx/documentation.md)
### Bloquear paises en el servidor web
Instalación de dependencias:
```sh
sudo apt update && sudo apt upgrade -y
sudo apt install libmaxminddb0 libmaxminddb-dev mmdb-bin nginx-module-geoip2 -y
```
Revisión existencia del módulo GeoIP^:
```sh
ls /usr/lib/nginx/modules/ | grep geoip
#Debe devolver ngx_http_geoip2_module.so
```
Crear cuenta en MaxMind, generar una licencia y descargue la base de datos `GeoLite2-Country.mmdb`.

Reubicar la base de datos:
```sh
sudo mkdir -p /etc/nginx/geoip
sudo cp GeoLite2-Country.mmdb /etc/nginx/geoip/
```
Asignar de permisos:
```sh
sudo chmod 644 /etc/nginx/geoip/GeoLite2-Country.mmdb
```
Aplicar módulo GeoIP:
```sh
sudo nano /etc/nginx/nginx.conf
#Agregar la siguiente linea antes de events{}
load_module modules/ngx_http_geoip2_module.so;
```
Agregar el siguiente contenido dentro de `/etc/nginx/nginx.conf` en el `http {}` ya existente:
```sh
http {
    geoip2 /etc/nginx/geoip/GeoLite2-Country.mmdb {
        $geoip2_country_code source=$remote_addr country iso_code;
    }
    map $geoip2_country_code $allowed_country {
        default yes;
        US no;
        MX no;
        AR no;
        CO no;
        CL no;
        PE no;
        BR no;
        VE no;
        EC no;
        BO no;
        PY no;
        UY no;
        DO no;
        CU no;
        GT no;
        HN no;
        NI no;
        SV no;
        CR no;
        PA no;
    }
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```

Editar la configuración de la página:
```sh
sudo nano /etc/nginx/sites-available/mipagina.es
```
Agregar lo siguiente, dentro de `server {}`:
```sh
server {
    listen 80;
    server_name mipagina.duckdns.org www.mipagina.duckdns.org;
    if ($allowed_country = no) {
        return 403;
    }
    root /var/www/mipagina.es;
    index index.html index.htm;
    location / {
        try_files $uri $uri/ =404;
    }
}
```
Recarga de nginx y comprobación:
```sh
sudo nginx -t
sudo systemctl reload nginx
```