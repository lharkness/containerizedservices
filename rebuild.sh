#!/bin/bash

# $1 is the name of the docker container
# $2 is the port it runs on

echo **** Starting [ $1 ] service on port [ $2 ]

docker stop $1
docker rm $1
docker build -t lharkness/$1 $1
docker run -d -p $2:$2 --name $1 lharkness/$1
