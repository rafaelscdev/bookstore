from rest_framework.test import APITestCase
from order.models.order import Order
from product.models.product import Product
from order.serializers.order_serializer import OrderSerializer

class TestOrderSerializer(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=100,
            active=True
        )
        self.order = Order.objects.create()
        self.order.products.add(self.product)
        self.order_serializer = OrderSerializer(instance=self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertIn('products', serializer_data)
        self.assertEqual(serializer_data['products'][0]['name'], self.product.name)
