#!/bin/bash -e
docker kill server client hacker || true
docker network rm common || true
docker network create common

docker run -tid\
	--rm\
	--name server\
	--network common\
	server
ip=$(docker inspect --format "{{ .NetworkSettings.Networks.common.IPAddress }}" server)
echo "ip is $ip"
docker run -tid\
	--rm\
	--name client\
	"--add-host=server.com:${ip}" \
	--network common\
	client
docker run -tid\
	--rm\
	--name hacker\
	"--add-host=server.com:${ip}" \
	--network common\
	hacker
