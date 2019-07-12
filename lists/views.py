"""Views of lists."""
from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    """View home page."""
    return render(request, 'home.html')


def view_list(request):
    """View user."""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    """Add user's item at list."""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
