"""List's Docstring - Forms configuration."""
from django import forms

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"


class ItemForm(forms.models.ModelForm):
    """Create form item."""

    class Meta:
        """Generate form with item."""

        model = Item
        fields = ('text',)
        widgets = {
            'text':
                forms.fields.TextInput(
                    attrs={
                        'placeholder': 'Enter a to-do item',
                        'class': 'form-control input-lg',
                    }),
        }
        error_messages = {'text': {'required': EMPTY_ITEM_ERROR}}
