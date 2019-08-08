"""List's Docstring - Forms configuration."""
from django import forms
from django.core.exceptions import ValidationError

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"


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

    def save(self, for_list):
        """Save a new item in the list."""
        self.instance.list = for_list
        return super().save()


class ExistingListItemForm(ItemForm):
    """Verify if the item is in the list."""

    def __init__(self, for_list, *args, **kwargs):
        """Init list to for_list."""
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        """Validate unique item in the list."""
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)

    def save(self):
        """Save a new item if the item is a unique item in the list."""
        return forms.models.ModelForm.save(self)
