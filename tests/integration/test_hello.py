import unittest
import requests

from tests.integration import HELLO_URL


class TestHello(unittest.TestCase):
    def test_hello(self):
        response = requests.get(HELLO_URL)
        self.assertEqual(200, response.status_code)
        self.assertEqual('Hello!', response.json()['message'])

if __name__ == '__main__':
    unittest.main()
