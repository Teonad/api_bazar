from django.urls import include, path
from rest_framework import routers

from products.views import ProductModelViewSet

app_name = 'products'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]