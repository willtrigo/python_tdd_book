"""TestCase of lists."""
from django.test import TestCase


class SmokeTest(TestCase):
    """Testcase of smoke."""

    def test_bad_maths(self):
        """Test bad maths."""
        self.assertEqual(1 + 1, 3)
