FROM python:3.8.6-alpine

ARG SRC_DIR=../app
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache  bash python3-dev build-base py-pip
RUN mkdir /app
WORKDIR /app
COPY $SRC_DIR/app/ /app/

RUN /bin/bash -c "source /app/bin/api"