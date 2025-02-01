import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory() 
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="mouse", price=100, category=[self.category])
        self.order = OrderFactory(product=[self.product])

        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_order(self):
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)
        self.assertEqual(order_data["results"][0]["product"][0]["title"], self.product.title)
        self.assertEqual(order_data["results"][0]["product"][0]["price"], self.product.price)
        self.assertEqual(order_data["results"][0]["product"][0]["active"], self.product.active)
        self.assertEqual(order_data["results"][0]["product"][0]["category"][0]["title"], self.category.title)

    def test_create_order(self):
        user = UserFactory()
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

        product = ProductFactory()
        data = {"products_id": [product.id], "user": user.id}

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )

        # Debug para entender possíveis erros
        print("Headers Enviados:", self.client._credentials)  # Verificar se o token está correto
        print("Response Status:", response.status_code)  # Verificar o status de resposta
        print("Response Data:", response.content)  # Verificar detalhes do erro

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Order.objects.filter(user=user).exists()) 
