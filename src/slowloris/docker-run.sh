#!/bin/bash -e
docker kill server client hacker || true
docker network rm common || true
docker network create common

docker run -tid\
	--rm\
	--name server\
	--network common\
	server
docker run -tid\
	--rm\
	--name client\
	--network common\
	client
docker run -tid\
	--rm\
	--name hacker\
	--network common\
	hacker
