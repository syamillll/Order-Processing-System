from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import DeliveryOrder, PurchaseOrder, Item, Inventory
from app.forms import AppForm
from django.core import serializers

# Create your views here.

@login_required
def confirmItem(request):
    data = serializers.serialize("python", Item.objects.all())
    doesNotExist = False
    notAvailable = False
    available = False

    try:
        if request.method == "POST":
            item_ID = request.POST["id"]
            ord_item = Item.objects.get(itemID=item_ID)
            item_name = ord_item.itemName
            inv_item = Inventory.objects.get(itemName=item_name)

            if inv_item.itemQuantity < ord_item.itemQuantity:
                notAvailable = True
            else:
                available= True        
    except Item.DoesNotExist:
        doesNotExist = True

    context = {
        "data": data, 
        "form": AppForm, 
        "notAvailable": notAvailable,
        "available": available,
        "doesNotExist": doesNotExist
    }
    context["user"] = request.user

    return render(request, "confirmItemAvailability/confirmItem.html", context)

