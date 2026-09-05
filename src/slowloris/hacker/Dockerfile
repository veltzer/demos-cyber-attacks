FROM python:3

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py /

CMD ["sleep", "3600"]
