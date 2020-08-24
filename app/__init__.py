from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from instance.config import *

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[APP_SETTINGS])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
