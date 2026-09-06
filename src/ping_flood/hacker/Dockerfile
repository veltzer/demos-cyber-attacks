FROM ubuntu:24.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get --yes upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends hping3 iputils-ping && \
    rm -rf /var/lib/apt/lists/*

COPY . /

CMD ["sleep", "3600"]
