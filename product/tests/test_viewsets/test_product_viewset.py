import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from product.factories import CategoryFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    def setUp(self):
        self.category = CategoryFactory(title="technology")
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_product(self):
        data = {
            "title": "Test Product",
            "price": 100,
            "category_id": [self.category.id],
            "active": True,
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )

        print("Response Status:", response.status_code)
        print("Response Data:", response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        product = Product.objects.get()
        self.assertEqual(product.title, "Test Product")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.category.first(), self.category)
        self.assertEqual(product.active, True)