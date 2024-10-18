from django.db import models
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

class ItemLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    description = MarkdownField(rendered_field='description_rendered', validator=VALIDATOR_STANDARD, default='')
    description_rendered = RenderedMarkdownField(null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    links = models.ManyToManyField(ItemLink, related_name='items', blank=True)
    name = models.CharField(max_length=255)
    notes = MarkdownField(rendered_field='notes_rendered', validator=VALIDATOR_STANDARD, default='')
    notes_rendered = RenderedMarkdownField(null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, related_name='items', blank=True)

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')
    alt = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.item.name}"
