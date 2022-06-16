from rest_framework import routers
from apps.wishes.views import WishViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'wishlist', WishViewSet, basename='products')
urlpatterns = [
    *router.urls
]