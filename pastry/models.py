import random
import hashlib

from flask import current_app as app

from pastry.db import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature


class User(object):
    def __init__(self, username, password):
        self.set_args(
            username=username,
            password=generate_password_hash(password)
        )

    def set_args(self, **kwargs):
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')

    def create(self):
        object_id = mongo.db.users.insert({
            'username': self.username,
            'password': self.password,
            'api_key': self.generate_api_key(),
        })
        return object_id

    def exists(self):
        user = mongo.db.users.find_one({'username': self.username})
        if user:
            self.set_args(**user)
            return True

    def generate_auth_token(self, expires_in=86400):
        s = TimedJSONWebSignatureSerializer(app.config.get('SECRET_KEY'), expires_in=expires_in)
        token = s.dumps({'username': self.username})
        return token

    def generate_api_key(self):
        return hashlib.md5(str(random.getrandbits(256))).hexdigest()

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def verify_api_key(api_key):
        return mongo.db.users.find_one({'api_key': api_key})

    @staticmethod
    def verify_auth_token(token):
        s = TimedJSONWebSignatureSerializer(app.config.get('SECRET_KEY'))
        try:
            data = s.loads(token)
        except SignatureExpired:
            # Valid token, but expired
            print 'expired token'
            return False
        except BadSignature:
            # Invalid token
            print 'invalid token'
            return False
        user = mongo.db.users.find_one({'username': data['username']})
        return user
