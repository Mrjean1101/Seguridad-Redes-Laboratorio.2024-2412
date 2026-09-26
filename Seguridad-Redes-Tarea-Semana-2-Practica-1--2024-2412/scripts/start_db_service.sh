#!/bin/bash

# Socket de escucha para simular DB en puerto 3306

python3 -m http.server 3306 --bind 10.24.12.131 &

echo "Servicio de BD escuchando en 10.24.12.131:3306"