from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product


class WishList(models.Model):
    name = models.CharField(max_length=30)
    product = models.ManyToManyField(User, through='wishes.WishListProduct')


class WishListProduct(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
