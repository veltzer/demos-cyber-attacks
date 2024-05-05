#!/bin/bash -e
docker kill server client hacker || true
docker run -tid\
	--rm\
	--name server\
	--sysctl 'net.ipv4.tcp_syncookies=0'\
	syn_flood_attack_server
docker run -tid\
	--rm\
	--name client\
	syn_flood_attack_client
docker run -tid\
	--rm\
	--name hacker\
	syn_flood_attack_hacker
