from rest_framework.test import APITestCase
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

class TestProductSerializer(APITestCase):
    def setUp(self):
        self.product_data = {
            "name": "Test Product",
            "description": "This is a test product",
            "price": 100,
            "active": True,
            "categories": []  # Adicione categorias se necessário
        }
        self.product = Product.objects.create(**self.product_data)
        self.product_serializer = ProductSerializer(instance=self.product)

    def test_product_serializer_fields(self):
        # Verifique os campos do serializer
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data['name'], self.product.name)
        self.assertEqual(serializer_data['description'], self.product.description)
        self.assertEqual(serializer_data['price'], self.product.price)
        self.assertEqual(serializer_data['active'], self.product.active)
