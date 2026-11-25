from django.db import models

# Create your models here.
class ProductDb(models.Model):
    product_name=models.CharField(max_length=100)
    product_code=models.CharField(max_length=100,unique=True)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    stock_quantity=models.IntegerField()

    def __str__(self):
        return self.product_name