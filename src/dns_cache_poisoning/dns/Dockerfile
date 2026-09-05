FROM python:3.7

RUN apt-get update && apt-get install --yes --no-install-recommends curl gnupg dnsutils iputils-ping net-tools && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir dnslib gevent

WORKDIR /src

COPY . .

ENTRYPOINT ["python", "server.py"]