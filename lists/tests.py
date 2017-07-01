"""Tests for the lists app.

"""
from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):
    """Test the home page.

    """

    def test_uses_home_page_template(self):
        """Checks that the home page template is used for /.

        :return:

        """

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
    """ORM test.

    """
    def test_saving_and_retrieving_items(self):
        """Checks that we can store and retrieve items in the database.

        """
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class ListViewTest(TestCase):
    """Tests for the list view.

    """
    def test_uses_list_template(self):
        """Check that we use the correct template.

        """
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        """Check that all items are displayed correctly.

        """
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        """Check that we store list items.

        :return:
        """
        self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_post(self):
        """Check that we redirect back to home page after storing list items.

        """
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
