#!/bin/bash -e
docker run -it --rm --user mark:mark --hostname demo --name demo demo bash --login -c "cd /home/mark; bash"
