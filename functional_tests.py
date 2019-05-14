"""Selenium test."""
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Test case of new visitor."""

    def setUp(self):
        """Init setup of new visitor."""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """End test of new visitor."""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Verify visitor."""
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # [...rest of comments as before]


if __name__ == '__main__':
    unittest.main(warnings='ignore')
