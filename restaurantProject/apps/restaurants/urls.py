from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'restaurant', RestaurantViewSet, basename='restaurant')
router.register(r'table', TableViewSet, basename='table')
router.register(r'tables_restaurant', TableViewSet, basename='tableRestaurant')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'bill', BillViewSet, basename='bill')
router.register(r'product_order', ProductOrderViewSet, basename='productOrder')

urlpatterns = []

urlpatterns += router.urls