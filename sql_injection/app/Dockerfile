FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install flask requests mysql-connector-python gunicorn
COPY wsgi.py app.py /
# CMD ["/app.py"]
CMD ["gunicorn","wsgi:app"]
