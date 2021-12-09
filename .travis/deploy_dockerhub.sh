#!/bin/sh
docker login --username=$DOCKER_USER --password=$DOCKER_PASS
docker build -f Dockerfile -t $NAMES:"latest" .
docker push $NAMES