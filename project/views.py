from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]

