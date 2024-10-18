from rest_framework import serializers
from ..models import Shopping
from products.api.serializers import ProductSerializer

class ShoppingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Shopping
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']
