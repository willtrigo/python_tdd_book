"""Models of lists."""
from django.db import models


class Item(models.Model):
    """Model itens of the list."""

    text = models.TextField(default='')
