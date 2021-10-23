FROM python:3.7-alpine
# MAINTAINER mdark1001
# unbuffered is recommend when python run whitin docker container
ENV PYTHONUNBUFFERED 1

# Install dependencies 
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
# Create app directory 
RUN mkdir /app 
# set directory above created
WORKDIR /app 
# 
COPY ./app /app

RUN  adduser -D django
USER django
