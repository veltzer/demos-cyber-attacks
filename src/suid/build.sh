#!/bin/bash -e
docker buildx build -t demo .
gcc finger.c -o finger.elf
