import base64
import hashlib

from app import db


class Users(db.Model):
    """Represents the user table."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    authtoken = db.relationship('AuthTokens', backref='users', lazy=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

    REQUIRED_FIELDS = {'username', 'password'}

    def init(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, encrypted_str):
        username_hash = hashlib.sha256(self.username.encode()).hexdigest()
        password_hash = hashlib.sha256(self.password.encode()).hexdigest()
        string_ = f'{password_hash}{username_hash}'
        encoded_str = base64.b64encode(string_.encode()).decode('utf-8')
        if isinstance(encrypted_str, bytes):
            encrypted_str = encrypted_str.decode('utf-8')
        return encoded_str == encrypted_str

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
