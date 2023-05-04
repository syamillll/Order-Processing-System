from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core import serializers
from app.models import PurchaseOrder, Item
from app.forms import AppForm
from django.db.models import Sum

# Create your views here.


@login_required
def submitPO(request):

    context = {"year": datetime.now().year, "form": AppForm}

    return render(request, "submitPurchaseOrder\submitPO_form.html", context)


@login_required
def submitPO_form(request):
    po_address = request.POST["deliveryAddress"]
    po_date = request.POST["deliveryDate"]
    po_client = request.user.username

    newPO = PurchaseOrder()
    newPO.deliveryAddress = po_address
    newPO.deliveryDate = po_date
    newPO.clientName = po_client
    newPO.totalPrice = 0.0

    newPO.save()

    context = {
        "form": AppForm,
        "purchaseID": newPO.purchaseID,
    }

    return render(request, "submitPurchaseOrder\submitPO_items.html", context)


@login_required
def submitPO_items(request):

    item_name = request.POST["itemName"]
    item_quantity = request.POST["itemQuantity"]
    item_price = request.POST["unitPrice"]
    po_ID = request.POST["purchaseID"]
    item_purchaseID = PurchaseOrder.objects.get(purchaseID=po_ID)

    newitem = Item()
    newitem.itemName = item_name
    newitem.itemQuantity = item_quantity
    newitem.unitPrice = item_price
    newitem.purchaseID = item_purchaseID
    newitem.save()

    newTotalPrice = float(item_price) * float(item_quantity)
    item_purchaseID.totalPrice = item_purchaseID.totalPrice + float("{:.2f}".format(newTotalPrice))
    item_purchaseID.save()

    data = serializers.serialize("python", Item.objects.filter(purchaseID=po_ID))

    context = {
        "form": AppForm,
        "purchaseID": po_ID,
        "data": data,
    }
    context["user"] = request.user

    return render(request, "submitPurchaseOrder\submitPO_items.html", context)
