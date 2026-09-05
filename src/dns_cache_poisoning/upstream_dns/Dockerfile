FROM python:3-alpine
# RUN apt-get update && apt-get install --yes --no-install-recommends curl gnupg dnsutils iputils-ping net-tools && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir dnslib gevent
COPY dns.py /
CMD ["/dns.py"]
