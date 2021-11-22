FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Required packages
RUN apt-get update -yqq && \
    apt-get install -qq ca-certificates gcc make \
    postgresql-server-dev-all python3-dev musl-dev \
    libffi-dev zlib1g-dev git bash g++ gcc \
    linux-headers-generic

WORKDIR /app
COPY . ./

# Dependencies
RUN pip3 install --upgrade pip
RUN pip install poetry
RUN poetry install
RUN pip install waitress

RUN chmod +x entrypoint.sh
