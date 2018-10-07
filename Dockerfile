FROM jfloff/alpine-python:3.6-slim AS build
ADD requirements_build.txt .
RUN echo "manylinux1_compatible = True" >> /usr/lib/python3.6/_manylinux.py && \
    apk add --no-cache --update build-base python3-dev musl-dev libffi-dev openssl-dev graphviz && \
    python -m pip install --upgrade pip wheel && \
    python -m pip install -r requirements_build.txt && \
    rm -rf /var/cache/apk/*
ADD requirements.txt .
RUN python -m pip install -r requirements.txt
ADD . /app
WORKDIR /app
