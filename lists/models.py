"""List's Docstring - Models configuration."""
from django.db import models
from django.core.urlresolvers import reverse


class List(models.Model):
    """Model user's list."""

    def get_absolute_url(self):
        """Set absolute URL."""
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """Model user's itens."""

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
