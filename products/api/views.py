from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Product
from .serializers import ProductSerializer
from base.views import IsOwnerOrSharedUser

class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    Listado de todos los productos
    
    .
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]  
    queryset = Product.objects.filter(state = True)
    
    def post(self, request, *args, **kwargs):
        """
        Creación de un producto
        
        .
        """
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrSharedUser]

    def get_queryset(self):
        return Product.objects.filter(
            shopping_list__user=self.request.user, state=True
        ) | Product.objects.filter(
            shopping_list__shared_with=self.request.user, state=True
        )
    
    def delete(self, request, pk=None):
        """
        Eliminación de un producto específico
        
        .
        """
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status= status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos!'}, status= status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        """
        Actualización de un producto específico
        
        .
        """
        
    def patch(self, request, *args, **kwargs):
        """
        Actualización parcial de un producto específico
        
        .
        """
    
    def get(self, request, *args, **kwargs):
        """
        Muestra de un producto específico
        
        .
        """
    