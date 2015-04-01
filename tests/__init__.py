import json

from pastry import create_app
from pastry.db import mongo
from pastry.models import User

from flask.ext.testing import TestCase


app = create_app('pastry.settings.TestConfig')


class PastryTest(TestCase):
    def create_app(self):
        self.test_username = 'user@test.com'
        self.test_password = 'password'
        return app

    def setUp(self):
        user = User(self.test_username, self.test_password)
        user.create()
        resp = self.client.post('/api/v1/login', data={
            'username': self.test_username,
            'password': self.test_password,
        })
        data = json.loads(resp.data)
        self.headers = {'Auth-Token': data['Auth-Token']}

    def tearDown(self):
        db_name = app.config['MONGO_URI'].split('/')[-1]
        mongo.cx.drop_database(db_name)
