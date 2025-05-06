import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        self.client.login(username='test_user', password='test_password')
        self.order = OrderFactory(user=self.user)
        self.list_url = reverse('order-list')
        self.detail_url = reverse('order-detail', kwargs={'pk': self.order.pk})

    def test_list_orders(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_order(self):
        data = {
            'user': self.user.pk,
            'product': self.order.product.pk,
            'quantity': 5
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    def test_delete_order(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)

    def test_order(self):
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)
        self.assertEqual(order_data["results"][0]["product"][0]["title"], self.order.product.title)
        self.assertEqual(order_data["results"][0]["product"][0]["price"], self.order.product.price)
        self.assertEqual(order_data["results"][0]["product"][0]["active"], self.order.product.active)
        self.assertEqual(order_data["results"][0]["product"][0]["category"][0]["title"], self.order.product.category.first().title)

    def test_create_order_with_token(self):
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