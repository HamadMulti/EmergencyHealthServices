from django.test import TestCase

# Create your tests here.
class BasicTest(TestCase):
    def test_basic_math(self):
        """Test basic arithmetic"""
        self.assertEqual(2 + 3, 5)
        self.assertEqual(-1 + 1, 0)
        self.assertNotEqual(2 + 2, 5)
    
    def test_homepage_exists(self):
        """Test that signin page loads"""
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

