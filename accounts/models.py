"""Account's Docstring - Models configuration."""
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class Token(models.Model):
    """Token user."""

    email = models.EmailField()
    uid = models.CharField(max_length=255)


class ListUserManager(BaseUserManager):
    """Model manager to ListUser."""

    def create_user(self, email):
        """Create user for manager."""
        ListUser.objects.create(email=email)

    def create_superuser(self, email, password):
        """Create superuser for manager."""
        self.create_user(email)


class ListUser(AbstractBaseUser, PermissionsMixin):
    """Minimal user model."""

    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email', 'height']

    objects = ListUserManager()

    @property
    def is_staff(self):
        """Staff email."""
        return self.email == 'willtrigo@example.com'

    @property
    def is_active(self):
        """Return state of the user."""
        return True
