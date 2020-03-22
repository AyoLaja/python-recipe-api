# Python image the project is based off of
# pyhton:3.7-alpine is a lightweight version of docker running the python image
FROM python:3.7-alpine
MAINTAINER Ayomide Onalaja <ayo.onalaja@gmail.com>

# Setting environment variable 
# Tells python to run in unbuffered mode: Doesnt allow python buffer variables, instead prints them directly
ENV PYTHONUNBUFFERED 1

# Install dependencies
# installs requirements.txt into the docker image with pip
# installs postgres ql client
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# make empty directory on docker image named /app
# switches /app to the default directory
# copy app folder from local machine to app folder in docker image
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create user that'll run application in docker
# USER user switches docker to the user recently created
RUN adduser -D user
USER user