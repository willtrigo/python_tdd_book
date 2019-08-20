"""Account's Docstring - Authentication configuration."""
from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):
    """Backend authentication."""

    def authenticate(self, uid):
        """Authenticate user with the uid."""
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        """Get user's list."""
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
