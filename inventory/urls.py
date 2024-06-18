from django.urls import path, include
from rest_framework import routers
from .views import InventoryItemViewSet, SupplierViewSet

router = routers.DefaultRouter()
router.register(r'inventory-items', InventoryItemViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
