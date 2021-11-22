from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    DateTime,
    ForeignKey,
    DECIMAL
)
from sqlalchemy.orm import declarative_base
from bonus.settings import engine

Base = declarative_base()

class Bonus(Base):
    __tablename__ = 'bonus'

    id = Column(Integer, primary_key=True)
    value = Column(DECIMAL)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    user_id = Column(ForeignKey("user.id"), nullable=True)

Base.metadata.create_all(engine)
