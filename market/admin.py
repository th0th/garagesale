from django.contrib import admin
from .models import Tag, Item, ItemImage, ItemLink

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1

class ItemLinkInline(admin.TabularInline):
    model = Item.links.through
    extra = 1

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(ItemLink)
class ItemLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'purchase_price', 'sale_price']
    search_fields = ['name', 'description']
    list_filter = ['tags']
    inlines = [ItemImageInline, ItemLinkInline]
    exclude = ('links',)
