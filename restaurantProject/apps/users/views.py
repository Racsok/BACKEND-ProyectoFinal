from datetime import datetime

#import rest_framework
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

#modelos
from apps.restaurants.models import Order
from .models import *
from .serializers import *
# Create your views here.

class WaiterViewSet(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializerModel
    permission_classes = [IsAuthenticated]
    
    
    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        waiter = self.get_object()
        print(f"{self.request.query_params} <---------------------------------->")
        if self.request.query_params.get('active') == '1':
            
            orders = Order.objects.all()
            serializer = Order.get_serializer(orders, many=True)
            print(orders)
            return Response(serializer.data)
        return Response({"hola": "hoola"})  
    
    
    
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
            return Response({"message": "Turno creado correctamente"})
        
        return Response(serializer.errors,)
    
    
    def filter_queryset(self, queryset):
        r_user = self.request.user
        queryset = queryset.filter(user = r_user)
        
        return queryset
    
class ShiftViewSet(ModelViewSet):
    queryset = WaiterShift.objects.all()
    serializer_class = WaiterShiftSerializer
    
    
