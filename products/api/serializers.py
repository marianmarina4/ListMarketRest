from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'quantity': instance.quantity,
            'price': instance.price,
        }

