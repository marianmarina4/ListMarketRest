from rest_framework import serializers
from ..models import Shopping
from products.api.serializers import ProductSerializer
from products.models import Product
from users.models import User

class ShoppingSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)
    shared_with = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all()) 

    class Meta:
        model = Shopping
        fields = ['id','name', 'shared_with', 'products']
        
    def create(self, validated_data):
        products_data = validated_data.pop('products', [])
        shared_with_data = validated_data.pop('shared_with', [])

        # Creamos la lista de compras
        shopping_list = Shopping.objects.create(**validated_data)

        # Añadimos los productos asociados a la lista de compras
        for product_data in products_data:
            Product.objects.create(shopping_list=shopping_list, **product_data)

        # Añadimos usuarios con quienes compartir
        shopping_list.shared_with.set(shared_with_data)

        return shopping_list

    def update(self, instance, validated_data):
        # Actualizamos el nombre de la lista
        instance.name = validated_data.get('name', instance.name)

        # Gestionar los productos (creación o actualización)
        products_data = validated_data.pop('products', [])
        existing_product_ids = [product.get('id') for product in products_data if product.get('id')]

        # Elimina productos no incluidos en la actualización
        instance.products.exclude(id__in=existing_product_ids).delete()
        
        for product_data in products_data:
            product_id = product_data.get('id', None)
            if product_id:
                # Actualizar producto existente
                product_instance = Product.objects.get(id=product_id, shopping_list=instance)
                product_instance.name = product_data.get('name', product_instance.name)
                product_instance.quantity = product_data.get('quantity', product_instance.quantity)
                product_instance.price = product_data.get('price', product_instance.price)
                product_instance.save()
            else:
                # Crear nuevo producto
                Product.objects.create(shopping_list=instance, **product_data)

        # Gestionar los usuarios con quienes compartir
        shared_with_data = validated_data.get('shared_with', [])
        if shared_with_data:
            instance.shared_with.set(shared_with_data)

        instance.save()
        return instance
    
    def validate_shared_with(self, value):
        if self.context['request'].user in value:
            raise serializers.ValidationError("No puedes compartir la lista contigo mismo.")
        return value


