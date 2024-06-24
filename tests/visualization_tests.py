import unittest
from services.visualization.app import app

class VisualizationTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_dashboard(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data Dashboard', response.data)

if __name__ == '__main__':
    unittest.main()
