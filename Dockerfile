FROM python:3.9.5-slim

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /app

# Set timezone
RUN echo "Asia/Dhaka" > /etc/timezone

# Install project dependencies
COPY ./requirements.txt .


RUN apt-get update \
    && pip install --upgrade pip \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && pip install -r requirements.txt

#
#RUN apt-get update \
#    && apt-get install build-essential python3-pip tzdata -y \
#    && pip3 install -r requirements.txt gunicorn \
#    && apt-get remove build-essential -y \
#    && apt-get autoremove -y \
#    && python3 manage.py migrate -y

# Copy project files
COPY . .
