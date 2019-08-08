"""Layout and styling Docstring."""
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    """Test case of layout and stying."""

    def test_layout_and_styling(self):
        """Verify page's layout and styling."""
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 612, delta=5)

        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')

        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 612, delta=5)
