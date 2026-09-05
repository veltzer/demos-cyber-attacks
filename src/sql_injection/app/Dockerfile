FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
COPY . /
CMD ["/run.py"]
