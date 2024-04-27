#!/bin/bash -e
# shellcheck source=compose/exercises/nodejs_postgresql/.env
source .env
docker-compose down
# docker volume rm nodejs_postgresql_postgres_data
