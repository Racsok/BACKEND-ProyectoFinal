from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

router = DefaultRouter()
router.register(r'waiters', WaiterViewSet, basename='waiters')
router.register(r'shift', ShiftViewSet, basename='shift')
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls