from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

# drf-yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

api_info = openapi.Info(
    title="Weather API",
    default_version='v1',
    description="API para gestionar temperaturas por ciudad. CRUD con Token Authentication.",
    contact=openapi.Contact(email="tu.email@ejemplo.com"),
    license=openapi.License(name="MIT License"),
)

SchemaView = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('temperatures.urls')),

    # Token Authentication
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Swagger y Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', SchemaView.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
