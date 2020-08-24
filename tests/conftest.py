"""Global fixtures for app."""

import pytest


from alembic.command import upgrade
from alembic.config import Config
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db


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
def client(request, manage, app):
    from models import Users

    def teardown():
        # clear table after each test.
        db.session.query(Users).delete()
        db.session.commit()

    request.addfinalizer(teardown)
    yield app.test_client()
