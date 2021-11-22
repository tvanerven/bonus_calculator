from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    DateTime,
    ForeignKey,
    DECIMAL,
    Boolean,
    String,
    Text
)
from sqlalchemy.orm import declarative_base
from bonus.settings import engine
from decimal import Decimal

Base = declarative_base()

class BasewithPrimaryKey(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

class Company(BasewithPrimaryKey):
    __tablename__ = 'company'

    name = Column(String)

class Scan(BasewithPrimaryKey):
    __tablename__ = 'scans'

    company = Column(ForeignKey('company.id'))
    is_internal = Column(Boolean, default=True)

class Dimension(BasewithPrimaryKey):
    __tablename__ = 'dimension'

    name = Column(String)
    scan = Column(ForeignKey('scan.id'))
    weight_factor = Column(Integer)

class DimensionResult(BasewithPrimaryKey):
    __tablename__ = 'dimension_result'

    dimension = Column(ForeignKey('dimension.id'))
    text = Column(Text)
    weight_low = Column(Integer)
    weight_high = Column(Integer)

class DimensionAspect(BasewithPrimaryKey):
    __tablename__ = 'dimension_aspect'

    dimension = Column(ForeignKey('dimension.id'))
    name = Column(String)
    weight_factor = Column(Integer)


class Question(BasewithPrimaryKey):
    __tablename__ = 'question'

    aspect = Column(ForeignKey('dimension_aspect.id'))
    text = Column(Text)
    question_type = Column(String)

class Answer(BasewithPrimaryKey):
    __tablename__ = 'answer'

    question = Column(ForeignKey('question.id'))
    answer = Column(Text)
