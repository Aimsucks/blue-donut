FROM python:3.8

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "sde_get_map"]