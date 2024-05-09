FROM python:3.12-alpine3.18
LABEL maintainer="https://www.roost.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /temp/requirements.txt
COPY ./requirements.dev.txt /temp/requirements.dev.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /temp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /temp/requirements.dev.txt ; \
    fi && \
    # rm -rf /temp && \
    adduser \
        --disabled-password \
        --no-create-home \
        djano-user

ENV PATH="/py/bin:$PATH"

USER djano-user

