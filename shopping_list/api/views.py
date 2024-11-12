from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from ..models import  Shopping
from .serializers import ShoppingSerializer
from base.views import IsOwnerOrSharedUser
from users.authentication_mixins import Authentication

class ShoppingListCreateAPIView(Authentication, generics.ListCreateAPIView):
    serializer_class = ShoppingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Creamos la lista de compras y sus productos asociados
        serializer.save(user=self.request.user, state=True)

    def get_queryset(self):
        # Filtra las listas de compras creadas por el usuario o compartidas con él
        return Shopping.objects.filter(
            Q(user=self.request.user) | Q(shared_with=self.request.user),
            state=True
        )
        
class ShoppingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingSerializer
    permission_classes = [IsOwnerOrSharedUser]

    def get_queryset(self):
        return Shopping.objects.filter(
            Q(user=self.request.user) | Q(shared_with=self.request.user),
            state=True
        )

    def perform_update(self, serializer):
        # Permite actualizar la lista de compras, incluyendo sus productos
        serializer.save()
    
    def delete(self, request, pk=None):
        shopping = self.get_queryset().filter(id=pk).first()
        if shopping:
            shopping.state = False
            shopping.save()
            return Response({'message':'Lista eliminada correctamente!'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe una lista con estos datos!'}, status= status.HTTP_400_BAD_REQUEST)
    
