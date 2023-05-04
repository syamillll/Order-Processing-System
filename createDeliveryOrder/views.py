from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core import serializers
from app.models import DeliveryOrder, PurchaseOrder, Item
from app.forms import AppForm, PurchaseIDSelector

# Create your views here.


@login_required
def createDO_form(request):
    context = {
        "year": datetime.now().year,
        "form": AppForm,
        "formFK": PurchaseIDSelector,
    }

    return render(request, "createDeliveryOrder\createDO_form.html", context)


@login_required
def createDO_item(request):

    do_address = request.POST["deliveryAddress"]
    do_date = request.POST["deliveryDate"]
    po_ID = request.POST["purchaseID"]
    do_purchaseID = PurchaseOrder.objects.get(purchaseID=po_ID)

    newDO = DeliveryOrder()
    newDO.purchaseID = do_purchaseID
    newDO.deliveryAddress = do_address
    newDO.deliveryDate = do_date

    newDO.save()

    data = serializers.serialize("python", Item.objects.filter(purchaseID=po_ID))

    context = {
        "year": datetime.now().year,
        "form": AppForm,
        "deliveryID": newDO.deliveryID,
        "purchaseID": po_ID,
        "data": data,
        "deliveryAddress": do_address,
        "deliveryDate": do_date
    }

    return render(request, "createDeliveryOrder\createDO_items.html", context)

