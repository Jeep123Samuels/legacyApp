"""Specie storages."""

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql.functions import func

from app import db
from helpers.utils import HelperModel


class Storages(db.Model, HelperModel):
    """Represents the Storages table."""

    __tablename__ = 'storages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255), index=True, unique=True, nullable=False)
    occurred_on = Column(DateTime, nullable=True)
    created_on = Column(DateTime, default=func.now(), nullable=False)
    total = Column(Float, nullable=False)

    REQUIRED_FIELDS = {'description', 'total', 'user_id'}

    @declared_attr
    def user_id(cls):
        return Column(Integer, ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return f'<Storages: {self.description} - {self.total}>'

    def to_dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data
