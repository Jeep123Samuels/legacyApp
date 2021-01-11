from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql.functions import func

from helpers.utils import HelperModel


class BaseModel(HelperModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    description = Column(String(255), index=True, unique=False, nullable=False)
    occurred_on = Column(DateTime, nullable=True)
    created_on = Column(DateTime, default=func.now(), nullable=False)

    REQUIRED_FIELDS = {'description', 'amount'}

    @declared_attr
    def storage_id(cls):
        return Column(Integer, ForeignKey('storages.id'), nullable=True)

    def to_dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data
