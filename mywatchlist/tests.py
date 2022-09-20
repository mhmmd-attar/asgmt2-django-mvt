from django.test import TestCase

class KatalogTest(TestCase):
    def testKatalogHTML_Exists(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def testKatalogXML_Exists(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def testKatalogJSON_Exists(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def testKatalogUsingTemplate(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertTemplateUsed(response, 'mywatchlist.html')