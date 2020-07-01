from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_cv_page(self):
        # Check cv page
        self.browser.get('http://localhost:8000/cv')

        # Check title
        self.assertIn('Bridging coursework', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('My blog', header_text)



if __name__ == '__main__':  
    unittest.main(warnings='ignore')