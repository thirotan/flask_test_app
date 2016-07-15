import unittest

from context import webapp

class TestApp(unittest.TestCase):

    def setUp(self):
        self.ap = webapp.app.test_client()

    def test_hello_world(self):
        response = self.ap.get('/')
        assert response.status_code == 200
        assert 'First App' in response.data

    def test_add(self):
        response = self.ap.post('/add', data=dict(
            comment='test'), follow_redirects=True)
        assert response.status_code == 200
        assert 'Hellotest!' in response.data

if  __name__ == '__main__':
    unittest.main()


