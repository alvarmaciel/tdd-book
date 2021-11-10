# Importo Selenium que manejará el navegadro y el componente webdriver
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):

        # Edit has heard about a cool new online to-do app. She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # Se notice the page title an header mention to-do list
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the Test")

        # She is invited to enter a to-do intem straight away

        # She types "Buy Peacock feathers" into a text box

        # When she hits enter, the page updates, ans now the page list
        # "1: Buy Peacock Feathers" as an item in a to-do list.

        # There is still a text box inviting her to add anothes item. She enters "Use
        # peacock feathers to make a fly"

        # The page updates again, and now shows both items in her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main()
