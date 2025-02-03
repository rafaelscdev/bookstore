from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny 

from product.models import Category
from product.serializers.category_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Category.objects.all().order_by("id")
