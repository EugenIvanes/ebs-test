from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from apps.wishes.serialisers import WishSerializer, WishAddSerializer
from apps.products.views import BasicModelViewSet
from apps.products.models import Product
from apps.wishes.models import WishList, WishListProduct
from django.db.utils import IntegrityError


class WishViewSet(BasicModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    serializer_class = WishSerializer
    queryset = WishList.objects.all()

    @action(detail=False, methods=["POST"],  url_path='add', permission_classes=[IsAuthenticated])
    @swagger_auto_schema(request_body=WishAddSerializer)
    def add_product_in_wishlist(self, request):
        data = request.data
        serializer = WishAddSerializer(data=data)
        if serializer.is_valid():
            WishListProduct.objects.create(product=Product.objects.get(id=serializer.data.get('product')),
                                           wishlist=self.queryset.get(id=serializer.data.get('wishlist')),
                                           user=request.user)
            return Response(serializer.data, status=201)
        return Response({'status': 'negative'})
