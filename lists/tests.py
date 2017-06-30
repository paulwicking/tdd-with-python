"""Tests for the lists app.

"""
from django.test import TestCase
from django.core.urlresolvers import resolve
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
