import sys
import unittest
sys.path.append("/home/elitsa/projects/week10/friday/source/model")
sys.path.append("/home/elitsa/projects/week10/friday/source")
from client import Client


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.test_client = Client("Ivo", 200000.00,
                                  "Bitcoin mining makes me rich")

    def test_client_name(self):
        self.assertEqual(self.test_client.get_username(), "Ivo")

    def test_client_balance(self):
        self.assertEqual(self.test_client.get_balance(), 200000.00)

    def test_client_message(self):
        self.assertEqual(self.test_client.get_message(),
                         "Bitcoin mining makes me rich")

    def test_add_client(self):
        test_client = Client('Maria')
        self.assertEqual(test_client, Client.add_client('Maria', '@bC7eF6h'))


if __name__ == '__main__':
    unittest.main()
