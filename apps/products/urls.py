from rest_framework import routers
from apps.products.views import ProductViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    *router.urls
]
