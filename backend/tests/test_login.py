from tests import PastryTest


class TestLogin(PastryTest):
    def test_login(self):
        resp = self.client.post('/api/v1/login', data={
            'username': self.test_username,
            'password': self.test_password,
        })
        assert resp.status_code == 200 and 'Auth-Token' in resp.data
