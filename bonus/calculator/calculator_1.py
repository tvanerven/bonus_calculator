import datetime
from decimal import Decimal
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from .models import Bonus
from bonus.settings.db import engine

class BonusTimeCalculator:

    def __init__(self, start_date, end_date, *args, **kwargs):
        self._start_date = start_date
        self._end_date = end_date
        self._check_date(start_date, end_date)
        self._session = sessionmaker(engine)
        self._raw_bonus_amount = None
        self._bonus_amount = None
        self.perform_calculation()

    @property
    def raw(self):
        return self._raw_bonus_amount

    @property
    def amount(self):
        return self._bonus_amount

    def _check_date(self, start_date, end_date):
        # Little sanity checking first.
        if end_date <= start_date:
            raise ValueError(
                "End date cannot be, or equal to start date"
            )

    def perform_calculation(self):
        bonus_objects = self._retrieve_bonus_objects()
        self._raw_bonus_amount = self._calculate_bonus(bonus_objects)
        rounded_bonus_amount = self._round_bonus_amount(
            self._raw_bonus_amount
        )
        self._bonus_amount = rounded_bonus_amount

    def _retrieve_bonus_objects(self):
        # Query. We need all bonus objects from the start date, since
        # we need to do partial calculations.
        with self._session() as session:
            session.query
        bonus_list = select(Bonus).where(
            Bonus.start_date >= self._start_date,
        ).order_by(
            Bonus.start_date.desc()
        )
        with self._session() as session:
            result = session.execute(bonus_list)
        return result.scalars().all()

    def _calculate_bonus(self, bonus_list):
        bonus_amount = Decimal('0.0')
        now = datetime.datetime.now()
        for bonus in bonus_list:
            if bonus.end_date >= now:
                # First case: The end date lies further in the future
                # than now. This means a partial bonus is in order.
                partial_bonus = self._do_partial_calculation(bonus, now)
            elif bonus.start_date <= self._start_date and bonus.end_date <= now:
                # Second case. The end case has passed, which means the full
                # bonus may be applied.
                bonus_amount += bonus.value
        return bonus_amount

    def _do_partial_calculation(self, bonus, datetime_now):
        unused_bonus_time = bonus.end_date - datetime_now
        used_bonus_time = bonus.end_time - unused_bonus_time
        consumed_bonus = self._get_bonus_per_month(bonus, used_bonus_time)
        return consumed_bonus

    def _get_bonus_per_month(self, bonus, timedelta):
        full_bonus_time = bonus.start_date - bonus.end_date
        value_per_month = bonus.value / full_bonus_time.months
        consumed_bonus = timedelta.months * value_per_month
        return value_per_month

    def _round_bonus_amount(self, bonus_amount):
        return bonus_amount + (bonus_amount%10)
