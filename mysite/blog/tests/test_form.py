from django.test import SimpleTestCase
from blog.forms import EmailPostForm
from blog.tests.test_ModelMixinTestCase import ModelMixinTestCase


class TestForms(ModelMixinTestCase, SimpleTestCase):
    def test_Email_form_valid_data(self):

        self.assertTrue(self.valide_form.is_valid())

    def test_Email_form_invalid_data(self):
        form = EmailPostForm(
            data={
                "name": "MadheshKumar",
                "email": 123,
                "to": "vjmadheshkumarofficial@gmail.com",
                "comments": "Read this post",
            }
        )

        self.assertFalse(form.is_valid())

    def test_Email_form_no_data(self):
        form = EmailPostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
