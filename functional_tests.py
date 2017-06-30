"""Functional test for an example to-do website.

Obey the Testing Goat.

"""
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #    Edith has heard about this rockin' new to-to app online.
        # She goes to check out the homepage:
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists:
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box.
        # (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as the item in a to-do list.

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly". Edith is very methodical.

        # The page updates again, and now shows both items on her list.

        # Edith wonders whter the site will remember her list. The she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
