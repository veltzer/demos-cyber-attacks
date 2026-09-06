FROM ubuntu:24.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get --yes upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends wget curl python3-requests python3 python-is-python3 && \
    rm -rf /var/lib/apt/lists/*

COPY . /

CMD ["sleep", "3600"]
