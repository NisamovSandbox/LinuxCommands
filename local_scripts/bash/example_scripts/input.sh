#!/bin/bash

# Solicitar al usuario que ingrese un valor numérico
read -p "Ingrese un valor numerico: " digito
# Comparacion de valor ingresado (supongo que es un numero)
if [ $digito -gt 10 ]; then
    echo "El valor ingresado '$digito' es mayor que 10."
elif [ $digito -eq 10 ]; then
    echo "El valor ingresado '$digito' es igual a 10."
else
    echo "El valor ingresado '$digito' no es mayor que 10."
fi