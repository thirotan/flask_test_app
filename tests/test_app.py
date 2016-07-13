import unittest

from context import webapp

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = webapp.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        assert response.status_code == 200


if  __name__ == '__main__':
    unittest.main()


