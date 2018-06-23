#!/usr/bin/env bash

echo 'Upgrading package lists...'
sudo apt-get update > /dev/null
sudo apt-get install -y docker.io docker docker-compose > /dev/null
