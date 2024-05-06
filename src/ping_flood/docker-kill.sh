#!/bin/bash -e
docker kill server client hacker || true
docker network rm flood || true
