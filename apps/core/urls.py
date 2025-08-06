from django.urls import path
from .views import WebsiteSettingsAPIView, WebsiteSettingAPIView

app_name = "core"

urlpatterns = [
    # API endpoints for website settings
    path("settings/", WebsiteSettingsAPIView.as_view(), name="website_settings_api"),
    path(
        "settings/<str:key>/",
        WebsiteSettingAPIView.as_view(),
        name="website_setting_api",
    ),
]
