#!/bin/bash -e
# shellcheck source=sql_injection/.env disable=SC2154,SC1091
source .env
xdg-open "http://${env_app_host}:${env_app_port}/"
