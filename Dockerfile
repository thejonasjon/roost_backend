FROM python:3.12-alpine3.18
LABEL maintainer="https://www.roost.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /temp/requirements.txt
COPY ./requirements.dev.txt /temp/requirements.dev.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

ARG DEV=true

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .temp-build-deps \
        build-base musl-dev postgresql-dev && \
    /py/bin/pip install -r /temp/requirements.txt && \
    if [ "$DEV" = "true" ]; \
        then /py/bin/pip install -r /temp/requirements.dev.txt ; \
    fi && \
    rm -rf /temp && \
    apk del .temp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        djano-user

ENV PATH="/py/bin:$PATH"

USER djano-user

