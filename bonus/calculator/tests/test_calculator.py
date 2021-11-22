import unittest
import datetime
from decimal import Decimal

from pyramid import testing
from bonus.calculator.calculator import BonusTimeCalculator
from bonus.calculator.factories import BonusFactory

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_start_time_not_before_end_time(self):
        start_time = datetime.datetime(year=2000, month=1, day=1)
        end_time = datetime.datetime(year=1900, month=1, day=1)
        with self.assertRaises(ValueError):
            calculator = BonusTimeCalculator(
                start_date=start_time,
                end_date=end_time
            )

    def test_bonus_calculated_correctly(self):
        start_time = datetime.datetime(year=2019, month=7, day=1)
        end_time = datetime.datetime(year=2021, month=1, day=1)
        BonusFactory(
            start_date=datetime.datetime(year=2019, month=1, day=1),
            end_date=datetime.datetime(year=2020, month=1, day=1),
            value=Decimal('100'),
            id=10
        )
        BonusFactory(
            start_date=datetime.datetime(year=2020, month=1, day=1),
            end_date=datetime.datetime(year=2021, month=1, day=1),
            value=Decimal('200'),
            id=10
        )
        calculator = BonusTimeCalculator(
            start_date=start_time,
            end_date=end_time
        )
        from IPython import embed; embed()
        self.assertEqual(
            calculator.amount,
            Decimal('250')
        )
