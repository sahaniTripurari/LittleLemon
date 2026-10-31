from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(title="Pizza", price=12.50, inventory=20)
        self.item2 = MenuItem.objects.create(title="Pasta", price=10.00, inventory=15)

    def test_getall(self):
        response = self.client.get('/api/menu-items/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
