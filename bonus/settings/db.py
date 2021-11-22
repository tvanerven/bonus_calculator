from sqlalchemy import create_engine
from os import getenv

user = getenv('POSTGRES_USER')
password = getenv('POSTGRES_PASSWORD')
database = getenv('POSTGRES_DB')

engine = create_engine(f'postgresql://{user}:{password}@db:5432/{database}', echo=True, future=True)
