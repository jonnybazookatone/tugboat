#!/bin/bash

docker stop tuboat
docker rm tugboat
docker build --tag adsabs/tugboat:$1 .
docker run -d --name tugboat -p 5000:80 -e API_DEV_KEY=$2 adsabs/tugboat:$1
