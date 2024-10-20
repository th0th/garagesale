# Generated by Django 5.1.2 on 2024-10-18 10:48

import django.db.models.deletion
import markdownfield.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', markdownfield.models.MarkdownField(default='', rendered_field='description_rendered')),
                ('description_rendered', markdownfield.models.RenderedMarkdownField(null=True)),
                ('is_sold', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('notes', markdownfield.models.MarkdownField(default='', rendered_field='notes_rendered')),
                ('notes_rendered', markdownfield.models.RenderedMarkdownField(null=True)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='items/')),
                ('alt', models.CharField(blank=True, max_length=255, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='market.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='links',
            field=models.ManyToManyField(blank=True, related_name='items', to='market.itemlink'),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='items', to='market.tag'),
        ),
    ]
