# shopping_list/serializers.py
from rest_framework import serializers
from ..models import Shopping, Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']

class ShoppingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Shopping
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']

