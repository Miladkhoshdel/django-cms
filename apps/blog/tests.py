from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.blog.models import BlogPost


class BlogPostAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="editor",
            password="secret-password",
        )
        self.client.force_authenticate(user=self.user)

    def test_create_blog_post(self):
        response = self.client.post(
            reverse("blog:blog-post-list"),
            {
                "title": "First Post",
                "excerpt": "Short intro",
                "content": "Full weblog content",
                "status": BlogPost.Status.PUBLISHED,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 1)

        post = BlogPost.objects.get()
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.slug, "first-post")
        self.assertIsNotNone(post.published_at)

    def test_filter_blog_posts_by_status(self):
        BlogPost.objects.create(title="Draft Post", content="Draft content")
        BlogPost.objects.create(
            title="Published Post",
            content="Published content",
            status=BlogPost.Status.PUBLISHED,
        )

        response = self.client.get(
            reverse("blog:blog-post-list"),
            {"status": BlogPost.Status.PUBLISHED},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Published Post")

    def test_retrieve_blog_post_by_slug(self):
        post = BlogPost.objects.create(
            title="Readable URLs",
            content="Use slugs for weblog URLs",
        )

        response = self.client.get(
            reverse("blog:blog-post-detail", kwargs={"slug": post.slug})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Readable URLs")
