from django.urls import path, include
from rest_framework import routers

from shop import views

router = routers.DefaultRouter()
router.register("shops", views.ShopViewSet, "shop")

urlpatterns = [
    path('', include(router.urls)),
]
