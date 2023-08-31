"""
write tests for this the different views using unittests
"""

import unittest  # import the python unit testing framework
from website import app   # import the Flask app object

# import the application code to be tested

# defines some test cases for the test case
class TestWebsite(unittest.TestCase):
    """
    define the test cases
    """

    def setUp(self):
        """
        sets up code that will run before each test
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """
        tests that the home page loads
        """
        result = self.app.get('/home')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Welcome to the home page', result.data)

    def test_about_page(self):
        """
        tests that the about page loads
        """
        result = self.app.get('/about')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'About', result.data)
        
    def test_contact_page(self):
        """
        tests that the contact page loads
        """
        result = self.app.get('/contact')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Contact', result.data)
    
    def test_index_page(self):
        """
        tests that the index recipes page loads
        """
        result = self.app.get('/index')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Index', result.data)

    def test_recipe_page(self):
        """
        tests that the recipe page loads
        """
        result = self.app.get('/recipe')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Recipe', result.data)    
# run the tests

if __name__ == '__main__':
    unittest.main()
    