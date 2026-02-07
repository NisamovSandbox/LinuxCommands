#!/bin/bash

while true; do
    echo "Este mensaje se muestra en un bucle infinito."
    sleep 2
done

var=0
while [ $var -lt 5 ]; do
    echo "El valor de la variable es: $var"
    var=$((var + 1))
    # Va sumando un digito por vuelta y cuando $var alcanza 5, el bucle termina
done