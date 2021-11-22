from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import scoped_session, sessionmaker

from bonus.calculator.models import Bonus
from bonus.settings.db import engine

session = scoped_session(sessionmaker(bind=engine))


class BonusFactory(SQLAlchemyModelFactory):

    class Meta:
        model = Bonus
        sqlalchemy_session = session
        sqlalchemy_get_or_create = ('id',)
