"""Tests for the lists app.

"""
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):
    """Test the home page.

    """
    def test_root_url_resolves_to_home_page_view(self):
        """Tests that url response is the expected view.

        :return: ``str``
        """
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """Checks that the home page wraps contents in <html></html> tags, and that the title is correct.

        :return:
        """
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
