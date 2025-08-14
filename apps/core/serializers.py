from rest_framework import serializers
from .models import WebsiteSettings


class WebsiteSettingsSerializer(serializers.ModelSerializer):
    """Serializer for WebsiteSettings model"""

    class Meta:
        model = WebsiteSettings
        fields = ["key", "value"]
        read_only_fields = ["id"]


class WebsiteSettingsKeyValueSerializer(serializers.Serializer):
    """Serializer to return settings as key-value pairs"""

    def to_representation(self, instance):
        """Convert queryset to key-value dictionary"""
        if hasattr(instance, "__iter__"):
            # If it's a queryset or list
            return {setting.key: setting.value for setting in instance}
        else:
            # If it's a single instance
            return {instance.key: instance.value}
