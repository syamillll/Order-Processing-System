from django.contrib import admin
from app.models import Item, PurchaseOrder, DeliveryOrder, RestockOrder, Inventory

admin.site.register(PurchaseOrder)
admin.site.register(Item)
admin.site.register(DeliveryOrder)
admin.site.register(RestockOrder)
admin.site.register(Inventory)
