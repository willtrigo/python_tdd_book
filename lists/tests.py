"""TestCase of lists."""
from django.test import TestCase


class HomePageTest(TestCase):
    """Test home page."""

    def test_uses_home_template(self):
        """Resolve url of home page."""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        """Verify html of home page."""
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')
