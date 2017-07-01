"""Tests for the lists app.

"""
from django.test import TestCase


class HomePageTest(TestCase):
    """Test the home page.

    """

    def test_home_page_returns_correct_html(self):
        """Checks that the home page wraps contents in <html></html> tags, and that the title is correct.

        :return:

        """

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
