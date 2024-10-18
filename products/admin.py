from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Product, ProductAdmin)