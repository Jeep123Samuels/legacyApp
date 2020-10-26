"""Global fixtures for app."""
from datetime import datetime, timedelta

import pytest

from alembic.command import upgrade
from alembic.config import Config
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db


@pytest.fixture
def test_user_data() -> dict:
    return {
        'password': 'cGFzc3dvcmQ=',
        'username': 'username',
    }


@pytest.fixture
def test_token() -> dict:
    return {
        'refresh_token': 'refresh_token',
        'token': 'token',
    }


@pytest.fixture(scope='session')
def app():
    """For some reason this needs to be defined again."""
    from flask import Flask
    from flask_restful import Api
    from instance.config import app_config, FLASK_ENV

    from api import register_views

    app = Flask('Test')
    app.config.from_object(app_config[FLASK_ENV])
    app_api = Api(app=app)
    register_views(api_obj=app_api)
    return app


@pytest.fixture(scope='session')
def manage(app):
    db.init_app(app)
    Migrate(app, db)
    manager = Manager(app)

    manager.add_command('db', MigrateCommand)

    # run migration command to create tables.
    with app.app_context():
        config = Config('migrations/alembic.ini')
        upgrade(config, 'head')
    db.create_all()
    db.session.commit()


@pytest.fixture
def client(request, manage, app, test_user_data, test_token):
    from models import AuthTokens
    from models import Users

    user = db.session.query(Users).filter_by(username=test_user_data['username']).first()
    if not user:
        user = Users(**test_user_data)
        user.save_instance()

    auth_token = db.session.query(AuthTokens).filter_by(user_id=user.id).first()

    test_token['user_id'] = user.id
    if not auth_token:
        test_token['expiry_date'] = datetime.now() + timedelta(hours=1)
        test_token['refresh_expiry_time'] = test_token['expiry_date']
        auth_token = AuthTokens(**test_token)
        auth_token.save_instance()

    def teardown():
        # clear table after each test.
        db.session.query(AuthTokens).delete()
        db.session.query(Users).delete()
        # db.session.commit()

    request.addfinalizer(teardown)
    yield app.test_client()
