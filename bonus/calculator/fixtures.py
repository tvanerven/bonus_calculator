import datetime
from decimal import Decimal

from .factories import BonusFactory

def load_data():
    data = [
        {
            'id': 1,
            'start_date': datetime.datetime(year=2019, month=1, day=1),
            'end_date': datetime.datetime(year=2020, month=1, day=1),
            'value': Decimal('100')
        },
        {
            'id': 2,
            'start_date': datetime.datetime(year=2020, month=1, day=1),
            'end_date': datetime.datetime(year=2021, month=1, day=1),
            'value': Decimal('200')
        }
    ]
    for item in data:
        BonusFactory.create(**item)
    print("Fixtures loaded!")
