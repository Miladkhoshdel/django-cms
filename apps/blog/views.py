from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(ListView):
    """Public page that renders published weblog posts."""

    model = BlogPost
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return BlogPost.objects.select_related("author").filter(
            status=BlogPost.Status.PUBLISHED
        )


class BlogPostDetailView(DetailView):
    """Public page that renders a single published weblog post."""

    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return BlogPost.objects.select_related("author").filter(
            status=BlogPost.Status.PUBLISHED
        )


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
