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
            title="title", author=self.test_user, body="body", status="draft"
        )
        self.test_post_object_publish = Post.objects.create(
            title="title2",
            author=self.test_user,
            body="body2",
            status="published",
        )
