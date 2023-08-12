from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('delivery/', views.delivery, name='delivery'),
    ]