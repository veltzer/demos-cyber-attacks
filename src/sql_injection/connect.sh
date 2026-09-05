#!/bin/bash -e
# shellcheck source=sql_injection/.env disable=SC2154,SC1091
source .env
mysql --host="127.0.0.1" --user="${env_db_user}" --port="${env_db_port_ext}" "${env_db_name}"
