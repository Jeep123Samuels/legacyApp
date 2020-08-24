
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db
from models import users
from instance.config import APP_SETTINGS, app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[APP_SETTINGS])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
