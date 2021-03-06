import os

from dotenv import load_dotenv

load_dotenv()

FLASK_APP = 'run.py'
APP_SETTINGS = os.getenv('APP_SETTINGS')
SECRET = 'a-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING'
FLASK_ENV = os.getenv('FLASK_ENV', APP_SETTINGS)


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET', SECRET)


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_DEV')


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TESTING')
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
# postgres://xxoablmkxbqsnv:cb34b9b7e6d87f13f28594f36573583a03f8cf4a5155d403c067ea2a9b8c39aa@ec2-54-234-28-165.compute-1.amazonaws.com:5432/d5i6th3sd66gd1