"""List's Docstring - Models configuration."""
from django.db import models


class List(models.Model):
    """Model user's list."""

    pass


class Item(models.Model):
    """Model user's itens."""

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
