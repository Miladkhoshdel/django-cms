from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class BlogPost(BaseModel):
    """A weblog post that can be published through the REST API."""

    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Published")
        ARCHIVED = "archived", _("Archived")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blog_posts",
        verbose_name=_("Author"),
    )
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        verbose_name=_("Slug"),
        help_text=_("URL-friendly identifier generated from the title if empty."),
    )
    excerpt = models.TextField(blank=True, verbose_name=_("Excerpt"))
    content = models.TextField(verbose_name=_("Content"))
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name=_("Status"),
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Published at"),
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()

        if self.status == self.Status.PUBLISHED and self.published_at is None:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title) or "post"
        slug = base_slug
        counter = 1
        queryset = type(self).objects.all()

        if self.pk:
            queryset = queryset.exclude(pk=self.pk)

        while queryset.filter(slug=slug).exists():
            counter += 1
            slug = f"{base_slug}-{counter}"

        return slug

    class Meta:
        ordering = ["-published_at", "-created_at"]
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["status", "-published_at"]),
        ]
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")
