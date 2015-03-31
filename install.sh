#!/bin/bash

serviceName=$1

ui_port=$(grep EXPOSE $serviceName/Dockerfile | cut -d ' ' --f 2)

echo installing [$serviceName] on port [$ui_port]


