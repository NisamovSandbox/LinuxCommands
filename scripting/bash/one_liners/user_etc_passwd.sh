# Script para mostrar un usuario dentro de `/etc/passwd`
cat /etc/passwd | grep "usuario" | cut -d: -f1
#cat y grep, muestran y limitan el campo a una sola linea del fichero donde se encuentra el usuario como texto `usuario`
#-d: = Define : como delimitador para separar la linea por partes
#-f1 = Usuario (antes del primer `:`)
#-f3 = UID
#-f6 = Directorio home
#-f7 = Shell