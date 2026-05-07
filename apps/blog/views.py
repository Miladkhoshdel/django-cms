from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    """REST API for weblog posts."""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    queryset = BlogPost.objects.select_related("author").all()

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get("status")

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
