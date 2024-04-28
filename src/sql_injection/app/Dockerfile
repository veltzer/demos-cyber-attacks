FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
COPY . /
RUN pip install -r requirements.txt
CMD ["/run.py"]
