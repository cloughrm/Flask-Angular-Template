import json

from pastry.db import mongo
from tests import PastryTest
from bson.objectid import ObjectId


class TestUsers(PastryTest):
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
