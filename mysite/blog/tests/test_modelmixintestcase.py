from django.test import TestCase, Client
from blog.models import Post
from django.contrib.auth.models import User
from django.urls import reverse


class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="maddy",
            password="123",
        )
        self.published_queryset = Post.published.all()

        self.draft_post = Post.objects.create(
            title="Draft",
            author=self.user,
            body="Testing Draft",
            status="draft",
        )
        self.published_post = Post.objects.create(
            title="Published",
            author=self.user,
            body="Testing Published",
            status="published",
        )

        self.list_url = reverse("blog:post_list")
        self.post_detail_url = reverse(
            "blog:post_detail",
            args=[
                self.published_post.publish.year,
                self.published_post.publish.month,
                self.published_post.publish.day,
                self.published_post.slug,
            ],
        )
