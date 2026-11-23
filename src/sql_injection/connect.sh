#!/bin/bash -e
# shellcheck source=src/sql_injection/.env
source .env
mysql --host="127.0.0.1" --user="${ENV_DB_USER}" --port="${ENV_DB_PORT_EXT}" "${ENV_DB_NAME}"
