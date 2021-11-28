#!/bin/sh
docker login --username=$DOCKER_USER --password=$DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker-compose build -f Dockerfile -t $NAMES:"latest" .
docker push $NAMES
