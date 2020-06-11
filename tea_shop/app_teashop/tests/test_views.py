from django.test import TestCase,Client
from django.urls import reverse
from app_teashop.models import Teashop
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('showprod',args=['1000'])

        self.args = Teashop.objects.create(
                    idno = 1000 ,
                    name='Green Tea',
                    description='nice tea',
                    price=99.00,
                    picture='shop_images/Green_tea_recipe.jpg',

        )
        #self.delete_url = reverse('delete_id')


    def test_createProduct_GET(self):

        response =  self.client.get(self.list_url)

        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_DisplayProduct_GET(self):

        response =  self.client.get(self.detail_url)

        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response, 'details.html')


