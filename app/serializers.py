from rest_framework.serializers import ModelSerializer
from . import models

class SerializedMenuItem(ModelSerializer):
    class Meta:
        model = models.Menuitem
        fields = "__all__"
        

class SerializedDeliveryCrew(ModelSerializer):
    class Meta:
        model = models.DeliveryCrew
        fields = "__all__"
        
        
class SerializedOrder(ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"
        
        
class SerializedCart(ModelSerializer):
    class Meta:
        model = models.Cart
        fields = "__all__"