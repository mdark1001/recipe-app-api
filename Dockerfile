FROM python:3.7-alpine
# MAINTAINER mdark1001
# unbuffered is recommend when python run whitin docker container
ENV PYTHONUNBUFFERED 1

# Install dependencies 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# Create app directory 
RUN mkdir /app 
# set directory above created
WORKDIR /app 
# 
COPY ./app /app

RUN  adduser -D django
USER django 
