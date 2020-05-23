from django.db import models

class Teashop(models.Model):

    idno=models.IntegerField(primary_key=True,max_length=10)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    images=models.ImageField(upload_to="shop_images",default=False)


