from django.shortcuts import render
from rest_framework import permissions

# Create your views here.

class IsOwnerOrSharedUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Verifica si el producto pertenece a una lista de compras cuyo propietario es el usuario
        if obj.user == request.user:
            return True
        # Verifica si el usuario tiene acceso compartido a la lista de compras
        if request.user in obj.shared_with.all():
            # Los usuarios compartidos pueden ver y actualizar, pero no eliminar
            return request.method in ['GET', 'PUT', 'PATCH']
        # Si no es el propietario ni un usuario compartido, deniega el acceso
        return False