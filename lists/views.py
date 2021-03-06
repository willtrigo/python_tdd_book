"""List's Docstring - View Configuration."""
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import List

User = get_user_model()


def home_page(request):
    """View home page."""
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    """Create new list."""
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


def view_list(request, list_id):
    """View user."""
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})


def my_lists(request, email):
    """View user's list."""
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})
