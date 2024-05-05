#!/bin/bash -e
docker kill server client hacker || true
docker network rm flood || true
docker network create\
	--attachable\
	--subnet=172.28.0.0/16\
	--ip-range=172.28.5.0/24\
	--gateway=172.28.5.254\
	flood

docker run -tid\
	--rm\
	--name server\
	--sysctl "net.ipv4.tcp_syncookies=0"\
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
	--cap-add CAP_NET_RAW\
	--privileged\
	hacker
