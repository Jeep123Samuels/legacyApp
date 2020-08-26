from uuid import uuid4

from app import db


class AuthTokens(db.Model):
    """Represents the authtokens table."""

    __tablename__ = 'authtokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String, nullable=False, default=uuid4)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    expiry_date = db.Column(db.DateTime, nullable=True, default=db.func.now())

    def __repr__(self):
        return f'<AuthToken: {self.user_id}'

    def to_dict(self):
        data = self.__dict__
        if data.get('expiry_date'):
            data['expiry_date'] = data.get('expiry_date').strftime("%d/%m/%Y, %H:%M:%S")
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data
