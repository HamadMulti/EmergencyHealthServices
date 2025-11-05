
    
    def test_homepage_exists(self):
        """Test that signin page loads"""
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
