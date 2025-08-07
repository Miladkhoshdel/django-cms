from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # Admin panel
    path("panel/", admin.site.urls),
    # JWT Authentication Endpoints
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # App Endpoints
    path("api/v1/core/", include("apps.core.urls", namespace="core")),
]
