from django.shortcuts import render
from .models import Item

# Create your views here.
def list_view(request):
    items = Item.objects.all()
    return render(request, 'market/list.html', {'items': items});


def detail_view(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'market/detail.html', {'item': item});
