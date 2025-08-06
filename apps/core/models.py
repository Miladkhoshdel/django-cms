from django.db import models
from .utils import upload_to
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """Base model with common fields."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WebsiteSettings(BaseModel):
    """
    Model to store website settings.

    This model is intended to store key-value pairs for configurable website settings,
    such as site title, contact email, theme options, or other global preferences.
    Each setting is uniquely identified by its 'key', and the corresponding 'value'
    can be any text relevant to the setting.

    Example usage:
        WebsiteSettings.objects.create(key="site_title", value="My Awesome Site")
        WebsiteSettings.objects.create(key="contact_email", value="info@example.com")
    """

    key = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Key"),
        help_text=_("Unique key for the setting"),
    )
    value = models.TextField(
        verbose_name=_("Value"), help_text=_("Value of the setting")
    )

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = _("Website Setting")
        verbose_name_plural = _("Website Settings")
