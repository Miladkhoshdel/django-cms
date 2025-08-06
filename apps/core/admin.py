from django.contrib import admin
from .models import WebsiteSettings


@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'created_at', 'updated_at')
    search_fields = ('key',)
    ordering = ('-created_at',)
