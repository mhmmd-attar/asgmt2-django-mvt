from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_wishlist_item = CatalogItem.objects.all()
    context = {
        'list_item': data_wishlist_item,
        'name': 'Mohammad Attar',
        'npm': '2106657992',
    }
    return render(request, "katalog.html", context)