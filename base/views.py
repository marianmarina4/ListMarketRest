from django.shortcuts import render
from rest_framework import permissions
from products.models import Product

# Create your views here.

class IsOwnerOrSharedUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Product):
            shopping_list = obj.shopping_list
        else:
            shopping_list = obj

        # Permite acceso si el usuario es el propietario o está en la lista compartida
        return shopping_list.user == request.user or request.user in shopping_list.shared_with.all()