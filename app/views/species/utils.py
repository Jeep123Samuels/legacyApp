from datetime import datetime

from sqlalchemy.sql import func

from app import db
from helpers.constants import DATE_TIME_FORMAT
from models import CreditEvents, DebitEvents, Storages


def _create_new_storage_mark(storage_obj, new_storage_total):
    now = datetime.now().strftime(DATE_TIME_FORMAT)
    obj: dict = dict(
        description=storage_obj.description,
        occurred_on=now,
        total=new_storage_total,
        user_id=storage_obj.user_id,
    )
    stor_obj = Storages(**obj)
    stor_obj.save_instance()


def get_current_storage_report(
    user_id: int,
    create_new_storage: bool = False,
    date_range: str = "",
):
    storages_desc: list = list()

    for storage_desc in db.session.query(
        Storages.description
    ).distinct(Storages.description).all():
        storages_desc.append(storage_desc[0])

    # get all Storages for a user
    storages = db.session.query(Storages).order_by(Storages.occurred_on.desc()).filter_by(
        user_id=user_id).filter(Storages.description.in_(storages_desc))
    now = datetime.now().strftime(DATE_TIME_FORMAT)

    if date_range:
        storages = storages.filter(Storages.occurred_on < date_range)
    storages = storages.limit(len(storages_desc)).all()

    print(storages)
    print(now)
    balances: dict = dict()
    variances: dict = dict()
    dates: dict = dict(
        past=storages[0].occurred_on,
        present=now,
    )
    for storage_ in storages:
        db_events = db.session.query(func.sum(DebitEvents.amount)).filter_by(
            storage_id=storage_.id
        ).filter(DebitEvents.occurred_on.between(storage_.occurred_on, now)).first()
        cd_events = db.session.query(func.sum(CreditEvents.amount)).filter_by(
            storage_id=storage_.id
        ).filter(CreditEvents.occurred_on.between(storage_.occurred_on, now)).first()

        db_events = db_events[0] if db_events[0] else 0
        cd_events = cd_events[0] if cd_events[0] else 0

        print(storage_.total)
        balances[storage_.description] = round(storage_.total + (db_events - cd_events), 2)
        if create_new_storage:
            _create_new_storage_mark(
                new_storage_total=balances[storage_.description],
                storage_obj=storage_,
            )

        variances[storage_.description] = round(balances[storage_.description] - storage_.total, 2)
    print(balances)
    print(variances)


print(get_current_storage_report(
    # create_new_storage=True,
    date_range="29-01-21",
    user_id=9,
))
