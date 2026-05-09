from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer for weblog posts."""

    author = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(required=False, allow_blank=True)

    def validate_slug(self, value):
        """Keep explicit slugs unique before hitting the database constraint."""
        if not value:
            return value

        queryset = BlogPost.objects.filter(slug=value)

        if self.instance is not None:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "A blog post with this slug already exists."
            )

        return value

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "excerpt",
            "content",
            "status",
            "published_at",
            "author",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at"]
