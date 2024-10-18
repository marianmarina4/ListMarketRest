from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name = 'usuario_list'),
    path('update/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name = 'usuario_update')
]
