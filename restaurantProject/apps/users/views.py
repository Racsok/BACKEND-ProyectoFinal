from datetime import datetime
from django.db.models import Q

#import rest_framework
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User

#modelos
from apps.restaurants.models import Order,Bill
from apps.restaurants.serializer import OrderSerializer
from .models import *
from .serializers import *
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializarModel
    

class WaiterViewSet(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializerModel
    permission_classes = [IsAuthenticated]
    
    
    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        waiter = self.get_object()
        orders = Order.objects.filter(waiter = waiter)
        serializer = OrderSerializer(orders, many=True)
        ordersActive = []
        if self.request.query_params.get('active') == '1':
            for order in orders:
                if(not Bill.objects.filter(order = order).exists()):
                    ordersActive.append(order)
                elif(Bill.objects.filter(order = order, finalCost = None).exists()):
                    ordersActive.append(order)
                    
            serializer = OrderSerializer(ordersActive, many=True)
            
        return Response(serializer.data)  
    
    
    
    @action(detail=True, methods=['post'])
    def add_shift(self, request, pk=None):
        waiter = self.get_object()
        serializer = WaiterShiftSerializer(data=request.data)
        
        if serializer.is_valid():
            start_date_str = request.data.get('start_date')
            end_date_str = request.data.get('end_date')
            restaurant_id = request.data.get('restaurant')
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
            
            shift = WaiterShift.objects.create(waiter=waiter, start_date=start_date, end_date=end_date, restaurant_id=restaurant_id)
            return Response({"message": "shift created "})
        
        return Response(serializer.errors,)
    
    
    
class ShiftViewSet(ModelViewSet):
    queryset = WaiterShift.objects.all()
    serializer_class = WaiterShiftSerializer
    permission_classes = [IsAuthenticated]
    
class TipWaiterViewSet(ModelViewSet):
    queryset = TipWaiter.objects.all()
    serializer_class = TipWaiterSerializer
    permission_classes = [IsAuthenticated]
    
    
