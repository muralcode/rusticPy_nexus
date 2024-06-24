import unittest
from services.processing_core.main import app

class ProcessingCoreTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_process_data(self):
        response = self.app.post('/process', json={'data': [1, 2, 3, 4]})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('transformed', data)
        self.assertIn('aggregated', data)
        self.assertIn('analysis', data)

if __name__ == '__main__':
    unittest.main()
