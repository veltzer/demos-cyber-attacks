#!/bin/bash -e
mysql --host="127.0.0.1" --user="${env_db_user}" "${env_db_name}"
