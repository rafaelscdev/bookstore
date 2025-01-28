from rest_framework import serializers
from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'category', 'category_id'] 

    def create(self, validated_data):
        category_data = validated_data.pop('category_id')
        
        product = Product.objects.create(**validated_data)
        for category_id in category_data:
            product.category.add(category)

        return product
