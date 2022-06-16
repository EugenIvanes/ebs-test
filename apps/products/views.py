from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.products.serializers import ProductSerializer
from apps.products.models import Product
from drf_util.views import BaseModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class BasicModelViewSet(BaseModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', ]
    search_fields = ['id', ]
    ordering_fields = ['id', ]
    ordering = ['-id', ]


class ProductViewSet(BasicModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    serializer_class = ProductSerializer
    queryset = Product.objects

    @action(detail=True,
            methods=['GET'],
            url_path='user/statistic')
    def user_statistic(self, request, pk=None):
        statistics = self.queryset.filter(id=pk).aggregate(Count('wishlistproduct__user_id', distinct=True))
        product = self.queryset.filter(id=pk).values()
        return Response({'users': statistics,
                        'product': product
                         })
