"""Base of Functional test's Docstring - Selenium configuration."""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import os

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    """Setup of the functional tests."""

    def setUp(self):
        """Init setup of new visitor."""
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        """End test of new visitor."""
        self.browser.quit()

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