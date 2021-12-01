
FROM python:3.9.6-alpine3.13 as dev

WORKDIR /work

RUN apk add build-base

FROM dev as runtime
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY ./src/api.py /app/api.py
COPY ./src/books.py /app/books.py
COPY ./src/settings.py /app/settings.py
COPY ./src/database.db /app/database.db

ENV FLASK_APP=api.py

CMD flask run -h 0.0.0 -p 5000