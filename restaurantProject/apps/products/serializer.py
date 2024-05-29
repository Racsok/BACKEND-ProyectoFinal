from rest_framework import serializers
from .models import Products

class ProductsSerializarModel(serializers.Serializer):
    class Meta:
        model = Products
        fields = "__all__"