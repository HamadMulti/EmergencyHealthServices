from django.test import TestCase

# Create your tests here.
import unittest
from test_auth import add_numbers

class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertNotEqual(add_numbers(2, 2), 5)

if __name__ == '__main__':
    unittest.main()

    
def test_user_login_flow(client):
    response = client.post("/login", data={"username": "test", "password": "1234"})
    assert response.status_code == 200
    assert b"Welcome" in response.data
