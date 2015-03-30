import os

# Flask settings
DEBUG = os.getenv('DEBUG', True)
SECRET_KEY = os.getenv('SECRET_KEY', 'danger_zone')

# Database settings
MONGO_USERNAME = os.getenv('MONGO_USERNAME', None)
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', None)
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_DBNAME = os.getenv('MONGO_DBNAME', 'pastry_dev')
