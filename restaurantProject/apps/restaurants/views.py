from datetime import datetime
from django.shortcuts import render

#import rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

#modelos
from apps.users.models import Waiter, WaiterShift
from .models import *
from .serializer import *
from .permissions import *
# Create your views here.

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    permission_classes = [IsAuthenticated]
    
class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        user = request.user
        try:
            waiter = Waiter.objects.get(user=user)
        except Waiter.DoesNotExist:
            return Response({"error": "El usuario no es un mesero."})

        current_datetime = datetime.now()
        try:
            # Obtener el turno actual del mesero para la fecha actual
            waiter_shift = WaiterShift.objects.get(waiter=waiter, start_date__lte=current_datetime, end_date__gte=current_datetime)
        except WaiterShift.DoesNotExist:
            return Response({"error": "No hay turno para este mesero en la fecha actual."})

        # Filtrar las mesas por el turno actual del mesero
        tables = Table.objects.all()
        # Serializar y devolver las mesas
        serializer = self.get_serializer(tables, many=True)
        return Response(serializer.data)
    
    
    
class TablesRestaurantViewSet(ModelViewSet):
    queryset = TablesRestaurant.objects.all()
    serializer_class = TablesRestaurantSerializer
    
    permission_classes = [IsAuthenticated]
    

    def list(self, request, *args, **kwargs):
        user = request.user
        try:
            waiter = Waiter.objects.get(user=user)
        except Waiter.DoesNotExist:
            return Response({"error": "El usuario no es un mesero."})

        current_datetime = datetime.now()
        try:
            waiter_shift = WaiterShift.objects.get(waiter=waiter, start_date__lte=current_datetime, end_date__gte=current_datetime)
        except WaiterShift.DoesNotExist:
            return Response({"error": "No hay turno para este mesero en la fecha actual."})

        tables = TablesRestaurant.objects.all()
        serializer = self.get_serializer(tables, many=True)
        return Response(serializer.data)
    
    
    
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == "destroy":
            return super().get_permissions() + [IsManagerOrder()]
        return super().get_permissions()
    
    
class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == "destroy":
            return super().get_permissions() + [IsManagerBIll()]
        return super().get_permissions()
        
    
    
class ProductOrderViewSet(ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    
    permission_classes = [IsAuthenticated]
