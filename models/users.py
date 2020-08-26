
from sqlalchemy import exc

from app import db
from auth_users.users import UsersModel
from helpers.utils import HelperModel, encrypt_password


class Users(db.Model, HelperModel, UsersModel):

    def save_instance(self):
        try:
            self.password = encrypt_password(self.password)
            db.session.add(self)
            db.session.commit()
            return
        except exc.SQLAlchemyError as e:
            return e
