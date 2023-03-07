from django.urls import path, include
from rest_framework import routers
from .views import AccountViewSet, TransactionViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
