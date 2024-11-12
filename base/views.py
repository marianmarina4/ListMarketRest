from django.shortcuts import render
from rest_framework import permissions

# Create your views here.

class IsOwnerOrSharedUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # El propietario puede hacer cualquier cosa
        if obj.user == request.user:
            return True
        # Los usuarios compartidos pueden ver y actualizar, pero no eliminar
        if request.user in obj.shared_with.all():
            return request.method in ['GET', 'PUT', 'PATCH']
        return False