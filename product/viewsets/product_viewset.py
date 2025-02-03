from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny  # Alterado para AllowAny
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')