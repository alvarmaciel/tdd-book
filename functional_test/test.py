# Importo Selenium que manejará el navegadro y el componente webdriver
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_tex):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_tex, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):

        # Edit has heard about a cool new online to-do app. She goes to check out its homepage
        self.browser.get(self.live_server_url)

        # Se notice the page title an header mention to-do list
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)
        # She is invited to enter a to-do intem straight away
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy Peacock feathers" into a text box
        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, ans now the page list
        # "1: Buy Peacock Feathers" as an item in a to-do list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail("Finish the test!")

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep