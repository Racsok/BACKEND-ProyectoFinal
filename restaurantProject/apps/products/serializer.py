from rest_framework import serializers
from .models import *

class ProductsSerializarModel(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        
class ProductsRestaurantASerializer(serializers.Serializer):
    class Meta: 
        model = ProductsRestaurant
        fields = "__all__"