"""Base of Functional test's Docstring - Selenium configuration."""
import sys
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    """Setup of the functional tests."""

    @classmethod
    def setUpClass(cls):
        """Set class setup."""
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    def setUp(self):
        """Init setup of new visitor."""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """End test of new visitor."""
        self.browser.quit()

    def wait_for(self, fn):
        """Wait function return something."""
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for_row_in_list_table(self, row_text):
        """Check text in the list."""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_item_input_box(self):
        """Get item input."""
        return self.browser.find_element_by_id('id_text')
