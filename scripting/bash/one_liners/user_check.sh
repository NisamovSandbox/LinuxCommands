# Comprobacion de la existencia de un usuario en el sistema
id <usuario_a_comprobar> 1>/dev/null 2>&1 && echo "El usuario existe" || echo "El usuario no existe"
#1>/dev/null: La salida por defecto de pantalla la redirije a /dev/null.
#2>&1: El output de errores, lo redirije a la misma direccion que la salida por defecto de errores, por lo que se redirije a /dev/null.