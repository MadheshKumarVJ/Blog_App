from django.test import TestCase, Client
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.urls import reverse
from blog.forms import EmailPostForm, CommentForm
from django.views.generic import ListView


class ModelMixinTestCase(TestCase):
    def setUp(self):

        self.client = Client()
        self.test_user = User.objects.create_user(
            username="maddy",
            password="123",
        )
        self.published_queryset = Post.published.all()

        self.draft_post = Post.objects.create(
            title="description",
            author=self.test_user,
            body="hi i am maddy",
            status="draft",
        )
        self.published_post = Post.objects.create(
            title="Test post thats status=published",
            author=self.test_user,
            body="This post is created by testuser author",
            slug="post-created-testuser-author",
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
        # Dont pass draft post in args (post 1 is a draft)
        self.post_share_url = reverse("blog:post_share", args=[2])

        self.Emailform = EmailPostForm(
            data={
                "name": "MadheshKumar",
                "email": "neomaddy104@gmail.com",
                "to": "vjmadheshkumarofficial@gmail.com",
                "comments": "Read this post",
            }
        )

        self.Commentform = CommentForm(
            data={
                "post": self.published_post,
                "name": "First comment",
                "email": "vjmadheshkumarofficial@gmail.com",
                "body": "this is comment body",
            }
        )

        self.add_tag = self.published_post.tags.add("test")
        self.tag = self.published_post.tags.first()

        self.post_list_by_tag = reverse(
            "blog:post_list_by_tag", args=[self.tag.slug]
        )
