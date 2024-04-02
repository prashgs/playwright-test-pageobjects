FROM python:3.11-slim

WORKDIR /app

COPY . /app
COPY requirements.txt /app/requirements.txt

RUN apt-get update && \
    apt-get install -y

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN playwright install chromium

CMD ["pytest", "--version"]
