from django.test import TestCase, SimpleTestCase

class simpleTest(SimpleTestCase):
    def test_it(self):
        response = self.client.get('/app/')
        self.assertEqual(response.status_code, 200)
    

