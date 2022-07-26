from django.contrib import admin
from django.urls import path, include

# api documentation imports
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# api documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Contacts List API",
        default_version='v1',
        description="An API for Contacts that is built in Django and DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="developer@me.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/contacts/', include('contacts.urls')),
    
    # api documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
 
]




