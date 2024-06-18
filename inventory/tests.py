from django.test import TestCase
from rest_framework.test import APIClient
from .models import InventoryItem, Supplier

class InventoryItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name='Test Supplier')
        self.item_data = {
            'name': 'Test Item',
            'price': 10.99,
            'suppliers': [self.supplier.id]
        }

    def test_create_inventory_item(self):
        response = self.client.post('/api/inventory-items/', self.item_data, format='json')
        print(response.content)  # Print the response content for debugging
        self.assertEqual(response.status_code, 201)
        self.assertEqual(InventoryItem.objects.count(), 1)

    def test_read_inventory_item(self):
        item = InventoryItem.objects.create(name='Test Item', price=10.99)
        response = self.client.get(f'/api/inventory-items/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Item')

    def test_update_inventory_item(self):
        item = InventoryItem.objects.create(name='Test Item', price=10.99)
        data = {'name': 'Updated Test Item'}
        response = self.client.patch(f'/api/inventory-items/{item.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(InventoryItem.objects.get(id=item.id).name, 'Updated Test Item')

    def test_delete_inventory_item(self):
        item = InventoryItem.objects.create(name='Test Item', price=10.99)
        response = self.client.delete(f'/api/inventory-items/{item.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(InventoryItem.objects.count(), 0)

class SupplierTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = InventoryItem.objects.create(name='Test Item', price=10.99)
        self.supplier_data = {
            'name': 'Test Supplier',
            'items': [self.item.id]
        }

    def test_create_supplier(self):
        response = self.client.post('/api/suppliers/', self.supplier_data, format='json')
        print(response.content)  # Print the response content for debugging
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Supplier.objects.count(), 1)

    def test_read_supplier(self):
        supplier = Supplier.objects.create(name='Test Supplier')
        response = self.client.get(f'/api/suppliers/{supplier.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Supplier')

    def test_update_supplier(self):
        supplier = Supplier.objects.create(name='Test Supplier')
        data = {'name': 'Updated Test Supplier'}
        response = self.client.patch(f'/api/suppliers/{supplier.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Supplier.objects.get(id=supplier.id).name, 'Updated Test Supplier')

    def test_delete_supplier(self):
        supplier = Supplier.objects.create(name='Test Supplier')
        response = self.client.delete(f'/api/suppliers/{supplier.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Supplier.objects.count(), 0)
