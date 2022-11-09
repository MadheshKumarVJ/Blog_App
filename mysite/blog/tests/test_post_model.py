from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class Post_Check(TestCase):
    def test_post_model(self):
        testuser = User.objects.create_user(username="maddy", password="12345")
        post = Post.objects.create(
            title="Sample Test", body="Iam Testing", author=testuser
        )

        self.assertEqual(str(post.title), "Sample Test")
        self.assertEqual(str(post.body), "Iam Testing")
        self.assertEqual(str(post.status), "draft")
        self.assertEqual((post.author), testuser)
