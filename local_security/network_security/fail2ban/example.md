# Fail2ban

Fail2ban es una herramienta de seguridad que protege servidores Linux contra ataques de fuerza bruta.
Monitorea logs del sistema y banea direcciones IP temporalmente tras múltiples intentos fallidos.

## Instalación
> Ubuntu/Debian
```bash
sudo apt update
sudo apt install fail2ban -y
```
> CentOS/RHEL/Fedora
```bash
sudo yum install epel-release -y
sudo yum install fail2ban -y
```
> Arch Linux
```bash
sudo pacman -S fail2ban
```
## Configuración Básica
Archivos de configuración principales
```bash
# Archivo de configuración principal
/etc/fail2ban/jail.conf # Se actualiza automaticamente tras actualizaciones
/etc/fail2ban/jail.local
# Configuraciones por servicio
/etc/fail2ban/jail.d/         # Configuraciones adicionales
/etc/fail2ban/filter.d/       # Filtros para diferentes servicios
/etc/fail2ban/action.d/       # Acciones a ejecutar
```
Configuración mínima (jail.local)
```ini
[DEFAULT]
# Direcciones IP a ignorar (no se tendran en cuenta)
ignoreip = 127.0.0.1/8 ::1 192.168.1.0/24
# Tiempo de baneo en segundos
bantime = 3600
# Ventana de tiempo para contar intentos
findtime = 600
# Número máximo de intentos antes del baneo
maxretry = 5
# Servicio a usar para baneo (iptables/ufw/etc.)
banaction = iptables-multiport
# Correo de notificación (opcional)
destemail = admin@dominio.com
sender = fail2ban@dominio.com
sendername = Fail2Ban
mta = sendmail
# Acción por defecto
action = %(action_)s
```
Protección de Servicios Comunes
## SSH (Puerto 22)
```ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 86400
```
## Apache/Nginx (Web)
```ini
[apache-auth]
enabled = true
port = http,https
filter = apache-auth
logpath = /var/log/apache2/error.log
maxretry = 3

[nginx-http-auth]
enabled = true
filter = nginx-http-auth
logpath = /var/log/nginx/error.log
maxretry = 3
```
## MySQL/MariaDB
```ini
[mysqld-auth]
enabled = true
filter = mysqld-auth
logpath = /var/log/mysql/error.log
maxretry = 3
port = 3306
```
## WordPress (Protección específica)
```ini
[wordpress]
enabled = true
filter = wordpress
logpath = /var/log/apache2/access.log
maxretry = 3
bantime = 86400
```
## Filtros Personalizados
Ejemplo: Detectar ataques SSH
Crea /etc/fail2ban/filter.d/sshd-custom.conf:
```ini
[Definition]
failregex = ^%(__prefix_line)sFailed password for invalid user .* from <HOST> port \d+ ssh2$
            ^%(__prefix_line)sFailed password for .* from <HOST> port \d+ ssh2$
            ^%(__prefix_line)sConnection closed by authenticating user .* <HOST> port \d+.*$
ignoreregex =
```
Ejemplo: Proteger PHPMyAdmin
Crea /etc/fail2ban/filter.d/phpmyadmin.conf:
```ini
[Definition]
failregex = ^<HOST> -.*"POST /phpmyadmin.* 200
            ^<HOST> -.*"POST /phpmyadmin.* 403
ignoreregex =
```
## Comandos Esenciales
Iniciar/Detener/Reiniciar
```bash
# Sistema con systemd
sudo systemctl start fail2ban
sudo systemctl stop fail2ban
sudo systemctl restart fail2ban
sudo systemctl status fail2ban
# Habilitar al inicio
sudo systemctl enable fail2ban
```
## Monitoreo y Gestión
```bash
# Ver estado general
sudo fail2ban-client status
# Ver estado de un jail específico
sudo fail2ban-client status sshd
# Banear una IP manualmente
sudo fail2ban-client set sshd banip 192.168.1.100
# Desbanear una IP
sudo fail2ban-client set sshd unbanip 192.168.1.100
# Añadir IP a lista blanca permanente
sudo fail2ban-client set sshd addignoreip 192.168.1.50
```
## Logs y Depuración
```bash
# Ver logs en tiempo real
sudo tail -f /var/log/fail2ban.log
# Ver baneos activos
sudo iptables -L -n
# Probar un filtro
sudo fail2ban-regex /var/log/auth.log /etc/fail2ban/filter.d/sshd.conf
```
## Configuraciones Avanzadas
Baneo por País
```bash
# Instalar geoiplookup
sudo apt install geoip-bin
# Crear filtro por país
# Bloquear IPs de países específicos
```
## Notificaciones por Telegram
```bash
#!/bin/bash
# Script de acción personalizada
TOKEN="tu_token"
CHAT_ID="tu_chat_id"
MESSAGE="IP <ip> baneada por <name>"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"
curl -s -X POST $URL -d chat_id=$CHAT_ID -d text="$MESSAGE"
```