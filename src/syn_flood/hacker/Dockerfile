FROM ubuntu:24.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get --yes upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends hping3 iputils-ping libcap2-bin python3 python3-scapy python-is-python3 && \
    rm -rf /var/lib/apt/lists/*

COPY . /

CMD ["sleep", "3600"]
