from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Menuitem)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.DeliveryCrew)