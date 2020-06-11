from django.test import TestCase
from app_teashop.models import Teashop


class TestModel(TestCase):
    def setUp(self):
        self.project = Teashop.objects.create(
            idno = 1000,
            name = 'Green Tea',
            description = "nice tea" ,
            price = 99.00 ,
            picture = "shop_images/Green_tea_recipe.jpg"

        )

    def test_teashop(self):
        self.assertEquals(self.project.idno, 1000)
        self.assertEquals(self.project.name,"Green Tea")
        self.assertEquals(self.project.description, "nice tea")
        self.assertEquals(self.project.price, 99.00)
        self.assertEquals(self.project.picture, "shop_images/Green_tea_recipe.jpg")
