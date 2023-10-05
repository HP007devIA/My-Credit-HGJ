import unittest
from fastapi.testclient import TestClient
from run import square_, app


class TestAPI(unittest.TestCase):
    client = TestClient(app)
    data = {'n' : 5}


    def test_response(self):
        reponse = self.client.post('/square', json=self.data)
        self.assertEqual(reponse.status_code, 200)


class Test_functions(unittest.TestCase):
    def test_return(self):
        self.assertEqual(square_(5), 25)
        self.assertEqual(square_(10), 100)
        self.assertEqual(square_(0), 0)
        self.assertEqual(square_(-5), 25)

    def test_type(self):
        self.assertEqual(type(square_(5)), int)

    def test_input_type(self):
        self.assertEqual(square_('-5'), 'Please enter a number')