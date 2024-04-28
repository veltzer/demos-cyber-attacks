#!/bin/bash -e
# shellcheck source=sql_injection/.env
source .env
mysql --host="127.0.0.1" --user="${env_db_user}" "${env_db_name}"
