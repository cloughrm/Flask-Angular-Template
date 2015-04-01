import json

from pastry import create_app
from pastry.db import mongo
from pastry.models import User

from bson.objectid import ObjectId

from flask.ext.testing import TestCase


app = create_app('pastry.settings.TestConfig')


class PastryTestBase(TestCase):
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

    def test_login(self):
        resp = self.client.post('/api/v1/login', data={
            'username': self.test_username,
            'password': self.test_password,
        })
        assert resp.status_code == 200 and 'Auth-Token' in resp.data

    def test_users_get_list(self):
        resp = self.client.get('/api/v1/users', headers=self.headers)
        data = json.loads(resp.data)
        assert resp.status_code == 200 and len(data['objects']) >= 1

    def test_users_post(self):
        resp = self.client.post('/api/v1/users', headers=self.headers, data={
            'username': 'new@user.com',
            'password': '1234',
        })
        data = json.loads(resp.data)
        new_user = mongo.db.users.find_one({'_id': ObjectId(data['id'])})
        assert new_user and new_user['username'] == 'new@user.com'
