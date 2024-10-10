from django.contrib import admin
from shopping_list.models import *

# Register your models here.

class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    
admin.site.register(Shopping, ShoppingAdmin)
admin.site.register(Product, ProductAdmin)
