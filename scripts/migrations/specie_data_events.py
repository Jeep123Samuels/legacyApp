
import sys

from app import db
from db_data import specie_data, users
from models import DebitEvents, CreditEvents, Storages, Users


def create_user_if_not_exist(data: dict):
    db_obj = db.session.query(Users).filter_by(username=data['username']).first()
    if db_obj:
        return db_obj.id

    user = Users(**data)
    user.save_instance()
    return user.id


def create_if_not_exist_db_entry(db_model, data):
    pass


def create_storages_from_data(users_id: int):
    for storage_ in specie_data['storages']:
        db_obj = db.session.query(Storages).filter_by(description=storage_['description']).first()

        if db_obj:
            continue

        storage_['user_id'] = users_id
        storages_ = Storages(**storage_)
        storages_.save_instance()


def create_debit_events_from_data():
    for d_event in specie_data['debit_events']:
        storage_ = specie_data['storages'][d_event['storage_id']]
        storage_obj = db.session.query(Storages).filter_by(description=storage_['description']).first()

        d_event['storage_id'] = storage_obj.id
        event_ = DebitEvents(**d_event)
        event_.save_instance()


def create_credit_events_from_data():
    for c_event in specie_data['credit_events']:
        storage_ = specie_data['storages'][c_event['storage_id']]
        storage_obj = db.session.query(Storages).filter_by(description=storage_['description']).first()

        c_event['storage_id'] = storage_obj.id
        event_ = CreditEvents(**c_event)
        event_.save_instance()


if __name__ == '__main__':
    user_id = create_user_if_not_exist(users[0])

    create_storages_from_data(users_id=user_id)

    create_debit_events_from_data()
    create_credit_events_from_data()
