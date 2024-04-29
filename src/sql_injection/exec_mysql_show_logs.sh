#!/bin/bash -e
docker-compose exec mysql tail -f /var/log/mysql.log
