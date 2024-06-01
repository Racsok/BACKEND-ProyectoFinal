from django.shortcuts import render

#import rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

#modelos
from .models import *
from .serializer import *
# Create your views here.

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    #permission_classes = [IsAuthenticated]
    
class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
    #permission_classes = [IsAuthenticated]
    
class TablesRestaurantViewSet(ModelViewSet):
    queryset = TablesRestaurant.objects.all()
    serializer_class = TablesRestaurantSerializer
    
    #permission_classes = [IsAuthenticated]
    
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
    #permission_classes = [IsAuthenticated]
    
class ProductOrderViewSet(ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    
    #permission_classes = [IsAuthenticated]
