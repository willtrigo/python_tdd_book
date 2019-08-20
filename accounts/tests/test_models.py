"""Account's models test Docstring."""
from django.contrib import auth
from django.test import TestCase

from accounts.models import Token

User = auth.get_user_model()


class UserModelTest(TestCase):
    """Test user account."""

    def test_user_is_valid_with_email_only(self):
        """Verify email valid."""
        user = User(email='a@b.com')
        user.full_clean()  # should not raise

    def test_email_is_primary_key(self):
        """Verify primary key of the email."""
        user = User(email='a@b.com')
        self.assertEqual(user.pk, 'a@b.com')

    def test_no_problem_with_auth_login(self):
        """If you create a custom user, you will need to verify the model without last_login field, because that field is used in auth, and it raise a error if you don't use in your custom user."""
        user = User.objects.create(email='edith@example.com')
        user.backend = ''
        request = self.client.request().wsgi_request
        auth.login(request, user)  # should not raise


class TokenModelTest(TestCase):
    """Test user's token."""

    def test_links_user_with_auto_generated_uid(self):
        """Verify generate token."""
        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertNotEqual(token1.uid, token2.uid)
