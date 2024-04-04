FROM python:3.11-slim

WORKDIR /app

COPY . .
COPY ./requirements.txt ./app/

RUN apt-get update && \
    apt-get install -y
RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt
RUN playwright install --with-deps chromium

CMD ["pytest", "/app/tests/test_sample.py"]
