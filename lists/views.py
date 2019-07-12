"""Views of lists."""
from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    """View home page."""
    return render(request, 'home.html')


def view_list(request, list_id):
    """View user."""
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    """Create new list."""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    """Add user's item at list."""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
