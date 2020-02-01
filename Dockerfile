FROM python:latest

RUN pip install poetry
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

EXPOSE 8000/tcp

COPY . /usr/blue_donut
WORKDIR /usr/blue_donut

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --workers=3"

RUN chmod +x /usr/blue_donut/entrypoint.sh
ENTRYPOINT ["/usr/blue_donut/entrypoint.sh"]
CMD ["gunicorn", "blue_donut.wsgi"]