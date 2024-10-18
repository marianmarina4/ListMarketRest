# Generated by Django 5.1 on 2024-10-17 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('shopping_list', '0006_remove_shopping_shared_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shopping_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='shopping_list.shopping'),
        ),
    ]
