from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/base.html')
        
class CVPageTest(TestCase):

    def test_uses_cv_home_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'blog/base.html', 'blog/cv.html')
    
    def test_can_save_a_POST_request(self):
	    response = self.client.post('/cv', data={'item_text': 'A new list item'})
	    self.assertIn('A new list item', response.content.decode())
	        