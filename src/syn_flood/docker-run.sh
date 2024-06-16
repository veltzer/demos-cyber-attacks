#!/bin/bash -e
docker kill server client hacker || true
docker network rm flood || true
docker network create flood

docker run -tid\
	--rm\
	--name server\
	--sysctl "net.ipv4.tcp_syncookies=1"\
	--network flood\
	server
docker run -tid\
	--rm\
	--name client\
	--network flood\
	client
docker run -tid\
	--rm\
	--name hacker\
	--network flood\
	hacker
