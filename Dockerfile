FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Creating working directory
RUN mkdir /app
WORKDIR /app

# Set timezone
RUN echo "Asia/Dhaka" > /etc/timezone

# Install project dependencies
COPY ./requirements.txt ./


RUN apt-get update \
    && apt-get install build-essential python3-pip tzdata -y \
    && pip3 install -r requirements.txt gunicorn \
    && apt-get remove build-essential -y \
    && apt-get autoremove -y


# Copy project files
COPY . .
