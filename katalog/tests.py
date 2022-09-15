from django.test import TestCase

class KatalogTest(TestCase):
    def testKatalogExists(self):
        response = self.client.get('/katalog/')
        self.assertEqual(response.status_code, 200)

    def testKatalogUsingTemplate(self):
        response = self.client.get('/katalog/')
        self.assertTemplateUsed(response, 'katalog.html')