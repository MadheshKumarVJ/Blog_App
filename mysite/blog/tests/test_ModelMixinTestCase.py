from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="maddy",
            password="123",
        )

        self.test_post_object_draft = Post.objects.create(
            title="Draft",
            author=self.test_user,
            body="Testing Draft",
            status="draft",
        )
        self.test_post_object_published = Post.objects.create(
            title="Published",
            author=self.test_user,
            body="Testing Published",
            status="published",
        )
