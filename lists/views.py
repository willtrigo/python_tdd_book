"""Views of lists."""
from django.http import HttpResponse


def home_page(request):
    """View home page."""
    return HttpResponse('<html><title>To-Do lists</title></html>')
