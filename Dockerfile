FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Required packages
RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc make postgresql-dev \
    python3-dev linux-headers musl-dev \
    libffi-dev zlib-dev \
    git bash g++ gcc

WORKDIR /app
COPY . ./

# Dependencies
RUN pip3 install --upgrade pip
RUN pip install poetry
RUN poetry install

RUN chmod +x entrypoint.sh
