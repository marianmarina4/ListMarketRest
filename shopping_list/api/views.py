from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import  Shopping
from .serializers import ShoppingSerializer
from base.views import IsOwnerOrSharedUser

class ShoppingListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ShoppingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        # Asignar el usuario autenticado a la nueva lista de compras
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Shopping.objects.filter(user= self.request.user, state = True)
        
class ShoppingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingSerializer
    permission_classes = [IsOwnerOrSharedUser]

    def get_queryset(self):
        # Devuelve solo las listas de compras del usuario autenticado
        return Shopping.objects.filter(user=self.request.user, state=True)
    
    def delete(self, request, pk=None):
        shopping = self.get_queryset().filter(id=pk).first()
        if shopping:
            shopping.state = False
            shopping.save()
            return Response({'message':'Lista eliminada correctamente!'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe una lista con estos datos!'}, status= status.HTTP_400_BAD_REQUEST)
