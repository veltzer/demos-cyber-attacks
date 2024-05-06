FROM ubuntu:latest

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get --yes upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends hping3 iputils-ping libcap2-bin python3 python3-scapy python-is-python3

COPY . /

CMD ["sleep", "3600"]
