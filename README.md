<!--
  _      _                     _____                                          _     
 | |    (_)                   / ____|                                        | |    
 | |     _ _ __  _   ___  __ | |     ___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
 | |    | | '_ \| | | \ \/ / | |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
 | |____| | | | | |_| |>  <  | |___| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
 |______|_|_| |_|\__,_/_/\_\  \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/
                                                                                    
Todos los derechos pertenecientes a Andrés Ruslan Abadías Otal | Nisamov: github.com/Nisamov
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #2f3136;
    color: #ffffff;
    line-height: 1.6;
    margin: 0;
    padding: 0px;
  }
  .doc-container {
    max-width: 800px;
    margin: 20px auto;
    background-color: #36393f;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.5);
  }
  .doc-header {
    text-align: left;
    margin-bottom: 20px;
  }
  .doc-header div {
    padding: 5px 0;
    font-weight: bold;
  }
  .doc-header a {
    color: #a69be9ff;
    text-decoration: none;
  }
  .doc-header a:hover {
    text-decoration: underline;
  }
  .separator {
    border-top: 2px solid #bdcabbff;
    border-radius: 2px;
    margin: 10px 0 20px 0;
  }
  h1, h2, h3 {
    color: #00b0f4;
    margin-top: 30px;
  }
  p, li {
    color: #ffffff;
  }
  a {
    color: #00b0f4;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
    color: #00b0f4;
  }
</style>
</head>
<body>

<div class="doc-container">
  <div class="doc-header">
    <div>Andrés Ruslan Abadías Otal</div>
    <div>Página web: <a href="https://github.com/Nisamov">Github</a></div>
    <div>Repositorio: <a href="https://github.com/Nisamov/LinuxCommands">Repositorio Origen</a></div>
    <div class="separator"></div>
  </div>
-->

![Cartel Principal](.github/media/LinuxCommandsWhiteTheme.png)

# LinuxCommands | Comandos y Servicios
<!--Todos los derechos pertenecientes a Andrés Ruslan Abadías Otal | Nisamov: github.com/Nisamov-->
Este repositorio está basado en los apuntes personales del creador [Andrés Ruslan Abadías Otal](https://github.com/Nisamov).

> Linux Commands es un repositorio concebido para todas aquellas personas que desean aprender a realizar distintos servicios en sistemas Linux, así como para quienes buscan información detallada y específica sobre los contenidos disponibles en el propio repositorio.

El formato de comandos establecido en ficheros `commands.md`, está basado en el [Documento de Origen](.github/origins/LinuxCommandsOrigen.md) creado el 15/07/2022, siendo [document_gestion/commands.md](/document_gestion/commands.md) el producto definitivo de ese mismo fichero.

[Más información a cerca del repositorio](.github/INFO.md)

### Estructura del Repositorio:

<!-- AUTO-GENERATED-INDEX:START -->
- document_management
  - [commands.md](/document_management/commands.md)
  - [compression.md](/document_management/compression.md)
  - [main.md](/document_management/main.md)
  - [theory.md](/document_management/theory.md)
- fundamentals
  - combination_keys
    - [combination.md](/fundamentals/combination_keys/combination.md)
  - system_structure
    - [linux-structure.md](/fundamentals/system_structure/linux-structure.md)
- networking
  - [commands.md](/networking/commands.md)
  - dhcp_failover
    - [manual.md](/networking/dhcp_failover/manual.md)
  - dhcp_samba
    - [theory.md](/networking/dhcp_samba/theory.md)
  - firewall_ufw
    - [commands.md](/networking/firewall_ufw/commands.md)
    - [theory.md](/networking/firewall_ufw/theory.md)
  - interfaces_net
    - [theory.md](/networking/interfaces_net/theory.md)
  - iptables
    - [command-list.md](/networking/iptables/command-list.md)
    - [commands.md](/networking/iptables/commands.md)
    - [theory.md](/networking/iptables/theory.md)
  - netplan_net
    - [theory.md](/networking/netplan_net/theory.md)
  - [theory.md](/networking/theory.md)
- permission_management
  - access_control_lists
    - [commands.md](/permission_management/access_control_lists/commands.md)
    - [theory.md](/permission_management/access_control_lists/theory.md)
  - [permissions.md](/permission_management/permissions.md)
  - [theory.md](/permission_management/theory.md)
- process_tasks
  - cron
    - [commands.md](/process_tasks/cron/commands.md)
    - [theory.md](/process_tasks/cron/theory.md)
- scripting
  - bash
    - example_scripts
    - [theory.md](/scripting/bash/theory.md)
- security
  - [audit.md](/security/audit.md)
  - proxy_squid
    - [documentation.md](/security/proxy_squid/documentation.md)
  - secure_channel
    - secure_channel_ftp
      - [documentation.md](/security/secure_channel/secure_channel_ftp/documentation.md)
      - [theory.md](/security/secure_channel/secure_channel_ftp/theory.md)
    - secure_channel_ssh
      - [documentation.md](/security/secure_channel/secure_channel_ssh/documentation.md)
      - [theory.md](/security/secure_channel/secure_channel_ssh/theory.md)
  - vpn_openvpn
    - [documentation.md](/security/vpn_openvpn/documentation.md)
- services
  - [commands.md](/services/commands.md)
  - [theory.md](/services/theory.md)
- software_management
  - [commands.md](/software_management/commands.md)
- storage
  - backup
    - [commands.md](/storage/backup/commands.md)
    - data_dump
      - [commands.md](/storage/backup/data_dump/commands.md)
      - [theory.md](/storage/backup/data_dump/theory.md)
    - [theory.md](/storage/backup/theory.md)
  - partitions
    - [commands.md](/storage/partitions/commands.md)
    - [theory.md](/storage/partitions/theory.md)
    - [virtualdisk.md](/storage/partitions/virtualdisk.md)
  - raid
    - [mount.md](/storage/raid/mount.md)
    - [theory.md](/storage/raid/theory.md)
- system_data
  - [packet_installation.md](/system_data/packet_installation.md)
  - [system_code.md](/system_data/system_code.md)
- users_permissions
  - [system_users.md](/users_permissions/system_users.md)
  - [user_management.md](/users_permissions/user_management.md)
- web_server
  - apache2
    - [documentation.md](/web_server/apache2/documentation.md)
  - nginx
    - GeoIP2
      - [documentation.md](/web_server/nginx/GeoIP2/documentation.md)
    - [documentation.md](/web_server/nginx/documentation.md)
  - wordpress
    - [documentation.md](/web_server/wordpress/documentation.md)
<!-- AUTO-GENERATED-INDEX:END -->
