FROM jfloff/alpine-python:3.6-slim
RUN echo "manylinux1_compatible = True" >> /usr/lib/python3.6/_manylinux.py && \
    apk add --no-cache --update build-base python3-dev musl-dev libffi-dev openssl-dev graphviz && \
    python -m pip install --upgrade pip wheel blockchain-etl && \
    rm -rf /var/cache/apk/*
ADD auto_ingest.py /app/auto_ingest.py
WORKDIR /app
CMD ["python3", "/app/auto_ingest.py"]
