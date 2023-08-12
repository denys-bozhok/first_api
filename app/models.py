from django.db import models
from django.utils.datetime_safe import datetime

from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Menuitem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    description = models.TextField()
    image = models.CharField(max_length=150, null=True)
    
    def __str__(self) -> str:
        return f'{self.name} : {self.description}'


class DeliveryCrew(models.Model):
    delivery_name = models.CharField(max_length=20)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    adress = models.CharField(max_length=200)
    cost = models.FloatField(default=0.00)
    
    def __str__(self) -> str:
        return f'{self.delivery_name}'


class Order(models.Model):
    user_id = models.CharField(max_length=50)
    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    products = models.ManyToManyField(Menuitem, blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def add_product():
        pass
    
    def delete_product():
        pass
    
    def change_count():
        pass
    
    def __str__(self) -> str:
        return f'{self.products} : {self.total}'