from django.test import TestCase
from django.test import Client

# Create your tests here.


class TestPage(TestCase):

    def test_index(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
