"""Views of lists."""
from django.shortcuts import render


def home_page(request):
    """View home page."""
    return render(request, 'home.html')
