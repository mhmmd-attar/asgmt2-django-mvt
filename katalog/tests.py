from django.test import TestCase, Client

class KatalogTest(TestCase):
    def testKatalogExists(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code, 200)

    def testKatalogUsingTemplate(self):
        response = Client().get('/katalog')
        self.assertTemplateUsed(response, 'katalog.html')