FROM python:3.6
MAINTAINER Angeline Meitzler

ENV INSTALL_PATH /api
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

RUN apt-get -y update
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

RUN echo "DROP DATABASE postgres"
RUN echo "CREATE DATABASE postgres"
RUN echo "CREATE DATABASE dbnlpizza"

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install scipy

ENV DJANGO_SETTINGS_MODULE=api.settings.production


COPY . .