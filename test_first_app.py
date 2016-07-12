import unittest

import first_app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = first_app.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        assert response.status_code == 200


if  __name__ == '__main__':
    unittest.main()


