#!/bin/bash -e
{ netstat -n -p TCP || true; } | grep SYN_RECV
