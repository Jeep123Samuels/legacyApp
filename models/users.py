import base64
import hashlib

from sqlalchemy import exc

from app import db
from helpers.utils import HelperModel, encrypt_password


class Users(HelperModel, db.Model):
    """Represents the user table."""

    __tablename__ = 'users'

    id = db.Column('user_id', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

    REQUIRED_FIELDS = {'username', 'password'}

    def is_correct_password(self, encrypted_str):
        string_ = base64.b64decode(encrypted_str.decode('utf-8')).decode('utf-8')
        return hashlib.sha256(string_.encode()).hexdigest() == self.password

    def __repr__(self):
        return f'<User: {self.username} - {self.email}>'

    def to_dict(self):
        data = self.__dict__
        if data.get('created_on'):
            data['created_on'] = data.get('created_on').strftime("%d/%m/%Y, %H:%M:%S")
        if data.get('updated_on'):
            data['updated_on'] = data.get('updated_on').strftime("%d/%m/%Y, %H:%M:%S")
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data

    def save_instance(self):
        try:
            self.password = encrypt_password(self.password)
            db.session.add(self)
            db.session.commit()
            return
        except exc.SQLAlchemyError as e:
            return e
