from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.views import index

# Swagger settings
schema_view = get_schema_view(
    openapi.Info(
        title="Booking System by Roberto Rodriguez",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.iamrobertorodriguez.com/",
        contact=openapi.Contact(email="iamrobertorodriguez@proton.me"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', index, name=""),
    path('admin/', admin.site.urls),

    # Including all models urls
    path("api/v1/", include("core.api.v1.urls")),

    # Token System
    path('api/v1/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #SWAGGER
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
