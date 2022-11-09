from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import post_list


class TestUrls(SimpleTestCase):
    def test_post_list_url_is_resolved(self):
        url = reverse("blog:post_list")
        self.assertEquals(resolve(url).func, post_list)
