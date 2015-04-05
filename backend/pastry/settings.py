import os


class BaseConfig(object):
    # Flask settings
    DEBUG = os.getenv('DEBUG', True)
    SECRET_KEY = os.getenv('SECRET_KEY', 'danger_zone')

    # Database settings
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost/pastry_dev')


class TestConfig(BaseConfig):
    MONGO_URI = 'mongodb://localhost/pastry_test'
    TESTING = True
