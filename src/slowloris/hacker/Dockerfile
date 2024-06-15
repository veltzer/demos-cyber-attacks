FROM python:3

RUN pip install --upgrade pip
COPY requirements.txt /
RUN pip install -r requirements.txt

COPY *.py /

CMD ["sleep", "3600"]
