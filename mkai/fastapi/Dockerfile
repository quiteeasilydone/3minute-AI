FROM python:3.9-alpine

WORKDIR /usr/src/fastapi_app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./app .