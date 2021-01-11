"""Specie that counts for total."""

from app import db
from models.specie.base import BaseModel


class DebitEvents(db.Model, BaseModel):
    """Represents the DebitEvents table."""

    __tablename__ = 'debit_events'

    def __repr__(self):
        return f'<DebitEvents: {self.description} - {self.amount}>'
