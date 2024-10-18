from django.db.models import Count
from django.shortcuts import render
from .models import Item, Tag
from django.template.defaultfilters import slugify


# Create your views here.
def list_view(request):
    tag_slug = request.GET.get('tag')

    if tag_slug:
        items = Item.objects.filter(tags__slug=tag_slug).all()
    else:
        items = Item.objects.all()

    tags = Tag.objects.annotate(count=Count('items')).order_by('-count')

    return render(
        request,
        'market/list.html',
        {'items': items, 'tags': tags, 'selected_tag': tag_slug}
    );


def detail_view(request, id):
    item = Item.objects.get(id=id)
    item_tags = item.tags.all()
    return render(request, 'market/detail.html', {'item': item, 'tags': item_tags});
