from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, ProdusctsRestaurantViewSet

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'products_restaurant', ProdusctsRestaurantViewSet, basename='productsRestauran')

urlpatterns = [
]

urlpatterns += router.urls