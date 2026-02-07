#!/bin/bash

# Variables definidas por el usuario
texto="Hola, Mundo!"
numero=42
pi=3.14
es_valido=true

#Variables de entorno
usuario=$USER
directorio_actual=$PWD
hogar=$HOME
sistema_operativo=$OSTYPE
fecha_actual=$(date)

# Estas variables pueden ser mostradas en la terminal de la siguiente manera:
echo "Variables definidas por el usuario:"
echo "Texto: $texto"
echo "Numero: $numero"
echo "Pi: $pi"
echo "Es valido: $es_valido"
echo ""
echo "Variables de entorno:"
echo "Usuario: $usuario"
echo "Directorio actual: $directorio_actual"
echo "Directorio hogar: $hogar"
echo "Sistema operativo: $sistema_operativo"
echo "Fecha actual: $fecha_actual"