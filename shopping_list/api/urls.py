from django.urls import path
from .views import (ShoppingListCreateAPIView, ShoppingRetrieveUpdateDestroyAPIView)
urlpatterns = [
    path('', ShoppingListCreateAPIView.as_view(), name='shopping_list'),
    path('<int:pk>/', ShoppingRetrieveUpdateDestroyAPIView.as_view(), name='shopping_update')
]
