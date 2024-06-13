import unittest
import app
import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_add(self):
        response = self.app.post('/add', 
                                  data=json.dumps(dict(num1=10, num2=5)), 
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], 15)

    def test_subtract(self):
        response = self.app.post('/subtract', 
                                  data=json.dumps(dict(num1=10, num2=5)), 
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], 5)

    def test_multiply(self):
        response = self.app.post('/multiply', 
                                  data=json.dumps(dict(num1=10, num2=5)), 
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], 50)

if __name__ == '__main__':
    unittest.main()