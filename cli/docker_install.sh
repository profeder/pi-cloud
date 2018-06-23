#!/usr/bin/env bash

echo 'Aggiornamento pacchetti in corso...'
sudo apt-get update > /dev/null

echo 'Ricerca componenti installati...'
compose="$(dpkg -l | grep docker-compose)"
echo $compose
if [ ! -z  $compose ]
then
    echo 'docker compose non installato'
    #apt-get install -y docker-compose
fi
