from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from ..models import Product, Shopping
from .serializers import ProductSerializer, ShoppingSerializer

class ShoppingListAPIView(generics.ListAPIView):
    serializer_class = ShoppingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Shopping.objects.filter(user= self.request.user, state = True)
    
    
    
class ShoppingCreateAPIView(generics.CreateAPIView):
    serializer_class = ShoppingSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        # Asignar el usuario autenticado a la nueva lista de compras
        serializer.save(user=self.request.user)
        
class ShoppingDetailAPIView(generics.RetrieveAPIView):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Devuelve solo las listas de compras del usuario autenticado
        return Shopping.objects.filter(user=self.request.user, state=True)        

    
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(state = True)
    serializer_class = ProductSerializer
    
    
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  