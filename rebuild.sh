#!/bin/bash

# $1 is the name of the docker container
# $2 is the port it runs on
#  additional ports can follow this

serviceName=$1

echo Starting [ $serviceName ] service  

docker stop $serviceName 
docker rm $serviceName
docker build -t lharkness/$serviceName $serviceName

dockerRunCmd=" run -d " 
for port in $(grep EXPOSE $serviceName/Dockerfile | cut -d ' ' --f 2-) 
do
	dockerRunCmd+=" -p $port:$port"
	shift
done

dockerRunCmd+=" --name $serviceName lharkness/$serviceName"

docker $dockerRunCmd
