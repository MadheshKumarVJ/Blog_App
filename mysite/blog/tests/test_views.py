from django.test import TestCase, Client
from blog.models import Post
from django.contrib.auth.models import User
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse("blog:post_list")
        self.detail_url = reverse(
            "blog:post_detail", args=[2022, 10, 11, "test"]
        )
        self.test_user = User.objects.create_user(
            username="maddy", password="123"
        )
        self.testpost = Post.objects.create(
            title="test", author=self.test_user, body="I am a test case"
        )

    def test_post_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/list.html")

    def test_post_deatil_POST(self):

        self.assertEquals(Post.objects.first().title, "test")
