FROM ubuntu:24.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get --yes upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends python3-pip python3-virtualenv net-tools && \
    rm -rf /var/lib/apt/lists/*

# This does not work
# RUN sysctl -w net.ipv4.tcp_syncookies=0

RUN virtualenv /venv
ENV PATH="/venv/bin:$PATH"
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
COPY . /
CMD ["/app.py"]
