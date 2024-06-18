from rest_framework import serializers
from .models import InventoryItem, Supplier

class InventoryItemSerializer(serializers.ModelSerializer):
    suppliers = serializers.PrimaryKeyRelatedField(many=True, queryset=Supplier.objects.all())

    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'price', 'date_added', 'suppliers']



class SupplierSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=InventoryItem.objects.all())

    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'items']
