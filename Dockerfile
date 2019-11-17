FROM python:3.8

ADD . /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]