from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    sku = models.CharField(max_length=12, db_index=True)
    price = models.IntegerField()
    description = models.TextField(null=True, )
