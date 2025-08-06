from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("panel/", admin.site.urls),
    path("api/v1/core/", include("apps.core.urls", namespace="core")),
]
