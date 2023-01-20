# base image
FROM python:3.8

# make required directories 
RUN mkdir -p /thumbnail_generator 

# set working directory
WORKDIR /thumbnail_generator 

# setup environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir media

# copy file from host to container
COPY . /thumbnail_generator/

# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

