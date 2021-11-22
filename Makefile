poetry:
	poetry install

start:
	docker-compose up -d

stop:
	docker-compose down

build:
	docker-compose build

test:
	docker-compose exec bonus_calculator_app_1 python -m pytest
