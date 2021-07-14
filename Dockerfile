# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install Flask

RUN pip3 install numpy

RUN pip3 install pandas

RUN pip3 install cassandra-driver

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]