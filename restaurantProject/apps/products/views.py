from django.shortcuts import render
from rest_framework.decorators import action

#import rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

#modelos
from .models import *
from .serializer import *
# Create your views here.

class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializarModel
    
    permission_classes = [IsAuthenticated]
    
    
