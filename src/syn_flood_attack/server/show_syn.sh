#!/bin/bash -e
netstat -n -p TCP  | grep SYN_RECV
