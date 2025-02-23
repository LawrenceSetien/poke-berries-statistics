import os
import requests
from unittest import TestCase
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

class PokeBerriesTest(TestCase):

    def test_get_all_berries_success(self):
        """
        Test the successful retrieval of all berry statistics from the API.
        """
        r = requests.get(f"{BASE_URL}/allBerryStats")
        self.assertEqual(200, r.status_code, r.content)
        self.assertIsNotNone(r.json(), 'Response not JSON')
        message = r.json()
        self.assertIsInstance(message, dict)
        self.assertIn("berries_names", message)
        self.assertIn("frequency_growth_time", message)
        self.assertIn("max_growth_time", message)
        self.assertIn("mean_growth_time", message)
        self.assertIn("median_growth_time", message)
        self.assertIn("min_growth_time", message)
        self.assertIn("variance_growth_time", message)
        self.assertIsInstance(message['berries_names'], list)
        self.assertIsInstance(message['frequency_growth_time'], dict)
        self.assertIsInstance(message['max_growth_time'], int)
        self.assertIsInstance(message['mean_growth_time'], float)
        self.assertIsInstance(message['median_growth_time'], float)
        self.assertIsInstance(message['min_growth_time'], int)
        self.assertIsInstance(message['variance_growth_time'], float)

    def test_get_histogram_success(self):
        """
        Test the /histogram endpoint for successful response.
        """
        r = requests.get(f"{BASE_URL}/histogram")
        self.assertEqual(200, r.status_code, r.content)
        self.assertIsNotNone(r.content, 'Response not HTML')
        self.assertIn(b'<img', r.content)

