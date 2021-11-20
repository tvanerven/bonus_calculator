poetry:
	poetry install

start:
	docker-compose up -d

stop:
	docker-compose down

build:
	docker-compose build
