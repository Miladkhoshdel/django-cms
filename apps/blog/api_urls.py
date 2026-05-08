from django.urls import include, path

from .routers import router

app_name = "blog_api"

urlpatterns = [
    path("", include(router.urls)),
]
