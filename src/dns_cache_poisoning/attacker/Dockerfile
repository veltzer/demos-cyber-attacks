FROM python:3.7

RUN pip install --no-cache-dir scapy

RUN apt-get update && apt-get install --yes --no-install-recommends curl gnupg dnsutils iputils-ping net-tools && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY . .

ENTRYPOINT ["/bin/bash"]
