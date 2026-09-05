FROM ubuntu:24.04

RUN apt-get update && apt-get install --yes --no-install-recommends curl gnupg dnsutils iputils-ping net-tools && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/sh", "-c", "echo nameserver 10.0.0.2 > /etc/resolv.conf && /bin/bash"]
