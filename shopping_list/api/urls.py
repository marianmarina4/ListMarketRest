from django.urls import path
from .views import ShoppingListAPIView, ShoppingCreateAPIView, ShoppingDetailAPIView, ProductListAPIView, ProductCreateAPIView

urlpatterns = [
    path('shopping', ShoppingListAPIView.as_view(), name='shopping'),
    path('shopping/<int:pk>', ShoppingDetailAPIView.as_view(), name='shopping_list'),
    path('shopping/create/', ShoppingCreateAPIView.as_view(), name='shopping_create'),
    path('products/', ProductListAPIView.as_view(), name='products_list'),
    path('products/create', ProductCreateAPIView.as_view(), name='products_create')
]
