from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Product
from .serializers import ProductSerializer
from base.views import IsOwnerOrSharedUser

class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]  
    queryset = Product.objects.filter(state = True)
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrSharedUser]

    def get_queryset(self):
        # Filtrar productos basados en si el usuario es el propietario o está en la lista compartida
        return Product.objects.filter(
            shopping_list__user=self.request.user, state=True
        )
    
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos!'}, status= status.HTTP_400_BAD_REQUEST)