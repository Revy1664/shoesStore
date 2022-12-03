from rest_framework import generics

from .models import Brand
from .serializers import BrandSerializer


class ListBrand(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class DetailBrand(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
