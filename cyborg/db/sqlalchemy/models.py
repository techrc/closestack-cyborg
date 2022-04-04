from cslo_db.sqlalchemy import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext import declarative


class CyborgBase(models.ModelBase):
    metadata = None


Base = declarative.declarative_base(cls=CyborgBase)


class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=True, unique=True)

