from django.test import TestCase
from blog.models import Post


class Publish_manager(TestCase):
    def test_published_manager(self):
        published_queryset = Post.published.get_queryset()
        objects_queryset_with_status_published = Post.objects.filter(
            status="published"
        )
        self.assertQuerysetEqual(
            published_queryset, objects_queryset_with_status_published
        )
