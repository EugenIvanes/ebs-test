from rest_framework import serializers
from apps.wishes.models import WishList, WishListProduct
from apps.products.serializers import ProductSerializer


class WishProductsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WishListProduct
        fields = ('product', 'wishlist')
        extra_kwargs = {
            'wishlist': {'write_only': True},
        }


class WishSerializer(serializers.ModelSerializer):
    products = WishProductsSerializer(many=True,
                                      source='wishlistproduct_set',
                                      read_only=True,
                                      required=False)

    class Meta:
        model = WishList
        fields = ('name', 'products')


class WishAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListProduct
        fields = ('wishlist', 'product')
