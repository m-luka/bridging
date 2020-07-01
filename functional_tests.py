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
        
        # Check form
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a CV item'
        )

        # Check input
        inputbox.send_keys('Education')
        
        # Check the page updates and the page lists the item
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Education' for row in rows)
        )
        
        # Text box still there, another CV item input
        self.fail('Finish the test!')
		
		# The page updates again, and now shows both items
		
		# Visit unique URL - items still there.



if __name__ == '__main__':  
    unittest.main(warnings='ignore')