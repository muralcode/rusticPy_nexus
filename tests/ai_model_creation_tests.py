import unittest
from services.ai_model_creation.app import app

class AIModelCreationTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_train_model(self):
        response = self.app.post('/train', json={
            'data': [[0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5]],
            'target': [0, 1, 0, 1]
        })
        self.assertEqual(response.status_code, 200)
        result = response.get_json()
        self.assertIn('accuracy', result)
        self.assertGreater(result['accuracy'], 0.0)

if __name__ == '__main__':
    unittest.main()
