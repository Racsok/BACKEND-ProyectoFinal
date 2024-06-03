from rest_framework.permissions import BasePermission
from apps.restaurants.models import Bill, Order


class IsManagerBill(BasePermission):
    def has_permission(self, request, view):
        bill = Bill.objects.filter(id=view.kwargs.get('pk'))
        if bill.exists():
            bill = bill.first()
            order = bill.order
            return order.waiter.charge == 'MG'
        else:
            return False
        
class IsManagerAtOrder(BasePermission):
    def has_permission(self, request, view):
        
        user = request.user
        order = Order.objects.filter(id=view.kwargs.get('pk'))
        if order.exists():
            order = order.first()
            waiter = order.waiter
            return waiter.charge == 'MG' or waiter.charge == 'AT'
        else:
            return False