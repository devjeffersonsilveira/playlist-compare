FROM python:3

WORKDIR /app
COPY . /app

run pip install -r playlist-compare/requirements/common.txt

EXPOSE 80
EXPOSE 5000
