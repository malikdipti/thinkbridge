from django.test import SimpleTestCase
from django.urls import reverse,resolve
from app_teashop.views import createProduct ,addProduct,DisplayProduct,deleteProduct

class TestUrls(SimpleTestCase):

   def test_create_product_resolve(self):
       url= reverse('list')
       self.assertEquals(resolve(url).func,createProduct)

   def test_add_product_resolve(self):
       url = reverse('addprod')
       self.assertEquals(resolve(url).func, addProduct)

   def test_displsy_product_resolve(self):
       url = reverse('showprod', args=['1000'])
       self.assertEquals(resolve(url).func.view_class, DisplayProduct)

   def test_delete_id_resolve(self):
       url = reverse('delete_id')
       self.assertEquals(resolve(url).func , deleteProduct)

