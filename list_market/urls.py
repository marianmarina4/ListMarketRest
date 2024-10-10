from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('users.api.urls')),
    path('shopping/', include('shopping_list.api.urls')),
]
