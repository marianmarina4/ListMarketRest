# Generated by Django 5.0.7 on 2024-10-04 13:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalItem',
            new_name='HistoricalProduct',
        ),
        migrations.RenameModel(
            old_name='Item',
            new_name='Product',
        ),
    ]
