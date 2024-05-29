#!/bin/bash -e
docker kill server client hacker || true
docker network rm common || true
