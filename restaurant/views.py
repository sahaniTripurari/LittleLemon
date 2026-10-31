from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Menu, Booking
from .serializers import MenuItemSerializer, MenuSerializer, BookingSerializer

# Static HTML homepage view
def index(request):
    return render(request, 'index.html', {})

# Menu Items Views
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Table Booking ViewSet (Secured with IsAuthenticated)
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
