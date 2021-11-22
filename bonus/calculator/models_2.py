from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    DateTime,
    ForeignKey,
    DECIMAL,
    Boolean
)
from sqlalchemy.orm import declarative_base
from bonus.settings import engine
from decimal import Decimal

Base = declarative_base()

class Bonus(Base):
    __tablename__ = 'bonus'

    id = Column(Integer, primary_key=True)
    value = Column(DECIMAL)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    user_id = Column(ForeignKey("user.id"), nullable=True)
    is_percentage = Column(Boolean)

Base.metadata.create_all(engine)


class Salary(Base):
    __tablename__ = 'salary'

    id = Column(Integer, primary_key=True)
    value = Column(DECIMAL)
    has_wage_discount = Column(Boolean, default=True)
    additional_pension = Column(DECIMAL, default=Decimal('0'))
    user_id = Column(ForeignKey("user.id"))

