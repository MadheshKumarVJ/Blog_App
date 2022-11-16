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
            slug="published",
        )

        self.second_published_post = Post.objects.create(
            title="Published2",
            author=self.user,
            body="Testing Published2",
            status="published",
            slug="published2",
        )

        self.third_published_post = Post.objects.create(
            title="Published3",
            author=self.user,
            body="Testing Published3",
            status="published",
            slug="published3",
        )

        self.fourth_published_post = Post.objects.create(
            title="Published4",
            author=self.user,
            body="Testing Published4",
            status="published",
            slug="published4",
        )

        self.five_published_post = Post.objects.create(
            title="Published5",
            author=self.user,
            body="Testing Published5",
            status="published",
            slug="published5",
        )
