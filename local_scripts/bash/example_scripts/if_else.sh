#!/bin/bash

# Definición de variables
digitobase=0
digitocomparar=5

# Ejemplo de estructura condicional IF-ELSE
if [ $digitobase -lt $digitocomparar ]; then
    echo "El valor de digitobase '$digitobase' es menor que digitocomparar '$digitocomparar'."
else
    echo "El valor de digitobase '$digitobase' no es menor que digitocomparar '$digitocomparar'."
fi

# Es posible comprimir el sript para optimizar espacio de la siguiente forma:
[ $digitobase -lt $digitocomparar ] && echo "'$digitobase' < '$digitocomparar'." || echo "$digitobase' !< '$digitocomparar'."
