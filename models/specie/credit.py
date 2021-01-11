"""Specie that counts against total."""

from app import db
from models.specie.base import BaseModel


class CreditEvents(db.Model, BaseModel):
    """Represents the Credit Events table."""

    __tablename__ = 'credit_events'

    def __repr__(self):
        return f'<CreditEvents: {self.description} - {self.amount}>'

