#!/bin/bash -e
# shellcheck source=src/sql_injection/.env
source .env
xdg-open "http://${env_app_host}:${env_app_port}/"
