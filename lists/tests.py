"""Tests for the lists app.

"""
from django.test import TestCase


class HomePageTest(TestCase):
    """Test the home page.

    """

    def test_uses_home_page_template(self):
        """Checks that the home page template is used for /.

        :return:

        """

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
