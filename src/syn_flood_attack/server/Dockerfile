FROM ubuntu:latest

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get --yes upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends python3-pip python3-virtualenv

RUN virtualenv /venv
ENV PATH="/venv/bin:$PATH"
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /
CMD ["/app.py"]
