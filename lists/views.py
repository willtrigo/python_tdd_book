"""Views of lists."""
from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    """View home page."""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'home.html')


def view_list(request):
    """View user."""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
