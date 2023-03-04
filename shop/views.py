from rest_framework import viewsets

from shop.models import Shop
from shop.serializers import ShopSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
