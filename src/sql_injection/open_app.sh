#!/bin/bash -e
# shellcheck source=src/sql_injection/.env
source .env
xdg-open "http://${ENV_APP_HOST}:${ENV_APP_PORT}/"
