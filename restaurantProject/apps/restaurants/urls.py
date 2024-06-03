from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurants')
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'tables_restaurant', TableViewSet, basename='tableRestaurant')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'bills', BillViewSet, basename='bills')
#router.register(r'product_order', ProductOrderViewSet, basename='productOrder')

urlpatterns = []

urlpatterns += router.urls