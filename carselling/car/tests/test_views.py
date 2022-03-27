import imp
from urllib import response
from django.test import TestCase , Client
from django.urls import reverse
from ..models import Car , BuyCar
import json

class TestViews(TestCase):

    def setUp(self):
        client = Client()
        self.cars_list_url = reverse('cars_list')
        self.thank_you_url = reverse('thank_you',args=[2])


    def test_cars_list_GET(self):
        response = self.client.get(self.cars_list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'car_list.html')

    def test_thank_you_GET(self):
        response = self.client.get(self.thank_you_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'thank_you.html')
