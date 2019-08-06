"""List's Docstring - Models configuration."""
from django.core.urlresolvers import reverse
from django.db import models


class List(models.Model):
    """Model user's list."""

    def get_absolute_url(self):
        """Set absolute URL."""
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """Model user's itens."""

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        """Set Meta item."""

        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        """Return text item."""
        return self.text
