from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login, Logout
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="List Market API",
      default_version='v1',
      description="Documentation List Market API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="marianomarina04@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('usuario/', include('users.api.urls')),
    path('login/', Login.as_view(), name= 'login'),
    path('logout/', Logout.as_view(), name= 'logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('shopping/', include('shopping_list.api.urls')),
    path('products/', include('products.api.urls')),
]
