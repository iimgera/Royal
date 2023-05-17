from django.urls import path, include
from rest_framework import routers

from .views import ImageViewSet


router = routers.DefaultRouter()
router.register(r'images', ImageViewSet, basename='image')

urlpatterns = [
    path('api/', include(router.urls)),
]
