from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core import serializers
from app.models import PurchaseOrder, Item, RestockOrder, Inventory
from app.forms import AppForm
from django.db.models import Sum

# Create your views here.


@login_required
def submitRO(request):
    data = serializers.serialize("python", Inventory.objects.all())

    context = {
        "data": data,
        "form": AppForm
    }

    return render(request, "submitRestockOrder\submitRO_warehouse.html", context)


@login_required
def submitRO_success(request):
    itemName = request.POST["itemName"]
    itemQuantity = request.POST["itemQuantity"]

    newRO = RestockOrder()
    newRO.itemName = itemName
    newRO.itemQuantity = itemQuantity

    newRO.save()

    context = {
        "form": AppForm,
        "RO": newRO,
    }

    return render(request, "submitRestockOrder\submitRO_success.html", context)



