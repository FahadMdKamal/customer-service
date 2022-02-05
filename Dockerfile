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

# Copy project files
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
