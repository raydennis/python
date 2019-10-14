import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UnmEDUTest(unittest.TestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome()
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_unmedu_search_for_duante_arruti(self):
        browser = self.browser
        browser.get('http://www.unm.edu')
        search_box = browser.find_element_by_id('unm_search_form_q')
        search_box.send_keys('Duane Arruti')
        search_box.send_keys(Keys.RETURN)
        # time.sleep(3)  # simulate long running test
        self.assertIn('Duane Arruti', browser.page_source)

    def tearDown(self):
        self.browser.quit()  


if __name__ == '__main__':
    unittest.main()
