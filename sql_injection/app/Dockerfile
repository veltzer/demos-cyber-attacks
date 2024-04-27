FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install flask requests mysql-connector-python gunicorn
COPY run_gunicorn.py wsgi.py app.py /
# CMD ["/app.py"]
# CMD ["gunicorn", "wsgi:app"]
# CMD ["gunicorn", "--bind", "${env_app_listen}:${env_app_port}", "wsgi:app"]
CMD ["/run_gunicorn.py"]
