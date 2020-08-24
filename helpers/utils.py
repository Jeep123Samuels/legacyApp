import hashlib

from sqlalchemy import exc

from app import db


def save_instance(instance):
    try:
        db.session.add(instance)
        db.session.commit()
        return
    except exc.SQLAlchemyError as e:
        return e


def delete_instance(instance):
    try:
        db.session.delete(instance)
        db.session.commit()
        return
    except exc.SQLAlchemyError as e:
        return e


def encrypt_password(password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if isinstance(password_hash, bytes):
        password_hash = password_hash.decode('utf-8')
    return password_hash
