FROM python:3-alpine
# RUN apt-get update && apt-get install curl gnupg dnsutils iputils-ping net-tools -y
RUN pip install dnslib gevent
COPY dns.py /
CMD ["/dns.py"]
