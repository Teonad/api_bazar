from django.urls import include, path
from rest_framework import routers

from products.views import ProductModelViewSet, BasketModelViewSet

app_name = 'products'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'baskets', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]