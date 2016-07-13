import unittest

from context import webapp

class TestApp(unittest.TestCase):

    def setUp(self):
        self.ap = webapp.app.test_client()

    def test_hello_world(self):
        response = self.ap.get('/')
        assert response.status_code == 200

    def test_add(self):
        response = self.ap.post('/add', data=dict(
            name='test'), follow_redirects=True)
        assert response.status_code == 200

if  __name__ == '__main__':
    unittest.main()


