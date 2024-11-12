# Generated by Django 5.0.7 on 2024-10-21 19:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0007_remove_product_shopping_list_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_shoppings', to=settings.AUTH_USER_MODEL),
        ),
    ]