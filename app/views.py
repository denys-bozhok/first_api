from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import SerializedMenuItem, SerializedDeliveryCrew, SerializedOrder, SerializedCart
from .models import Menuitem, Cart, Order, DeliveryCrew

# Create your views here.


@api_view(['GET'])
def home(request):
    menu_items = Menuitem.objects.all()
    ser_menu_items = SerializedMenuItem(menu_items, many = True)
    data = ser_menu_items.data
    
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def delivery(request):
    delivery_crews = DeliveryCrew.objects.all()
    ser_delivery_crews = SerializedDeliveryCrew(delivery_crews, many = True)
    data = ser_delivery_crews.data
    
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'DELETE'])
def cart(request):
    carts = Cart.objects.all()
    ser_carts = SerializedCart(carts, many = True)
    data = ser_carts.data
    
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'DELETE'])
def order(request):
    orders = Order.objects.all()
    ser_orders = SerializedCart(orders, many = True)
    data = ser_orders.data
    
    return Response(data, status=status.HTTP_200_OK)
