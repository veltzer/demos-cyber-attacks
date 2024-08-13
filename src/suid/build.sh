#!/bin/bash -e
gcc finger.c -o finger.elf
docker buildx build -t demo .
