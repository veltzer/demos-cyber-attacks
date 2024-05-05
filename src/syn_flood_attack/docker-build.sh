#!/bin/bash -e
for x in server hacker client
do
	cd $x
	docker buildx build -t "$x" .
	cd ..
done
