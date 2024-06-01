from datetime import datetime
from django.shortcuts import render

#import rest_framework
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

#modelos
from .models import *
from .serializers import *
# Create your views here.

class WaiterViewSet(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializerModel
    #permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['post'])
    def add_shift(self, request, pk=None):
        waiter = self.get_object()
        serializer = WaiterShiftSerializer(data=request.data)
        print(request.data)
        
        if serializer.is_valid():
            start_date_str = request.data.get('start_date')
            end_date_str = request.data.get('end_date')
            restaurant_id = request.data.get('restaurant')
            print(start_date_str)
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
            
            shift = WaiterShift.objects.create(waiter=waiter, start_date=start_date, end_date=end_date, restaurant_id=restaurant_id)
            return Response({"message": "Turno creado correctamente"})
        
        return Response(serializer.errors,)
    
    
    # def filter_queryset(self, queryset):
    #     r_user = self.request.user
    #     queryset = queryset.filter(user = r_user)
        
    #     return queryset
    
    
