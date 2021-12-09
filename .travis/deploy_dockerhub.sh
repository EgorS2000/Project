#!/bin/sh
docker login --username=$DOCKER_USER --password=$DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker-compose build

docker tag web $DOCKER_USER/project_web
docker tag web $DOCKER_USER/project_nginx
docker tag web $DOCKER_USER/project_db

docker push $DOCKER_USER/project_web:"latest"
docker push $DOCKER_USER/project_nginx:"latest"
docker push $DOCKER_USER/project_db:"latest"
