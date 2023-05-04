from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import (
    DeliveryOrder,
    PurchaseOrder,
    Item,
    Status,
    RestockOrder,
    Inventory,
)
from app.forms import AppForm
from django.core import serializers

# Create your views here.


@login_required
def verifyRO(request):
    data = serializers.serialize("python", RestockOrder.objects.all())

    context = {
        "data": data,
        "form": AppForm,
    }
    context["user"] = request.user

    return render(request, "verifyRestockOrder/verifyRO_table.html", context)


@login_required
def verifyRO_compare(request):
    try:
        restock_ID = request.POST["id"]
        selected_RO = RestockOrder.objects.get(restockID=restock_ID)
        data = serializers.serialize("python", Inventory.objects.all())

        context = {
            "data": data,
            "RO": selected_RO,
        }
        context["user"] = request.user

        return render(request, "verifyRestockOrder/verifyRO_compare.html", context)

    except RestockOrder.DoesNotExist:
        data = serializers.serialize("python", RestockOrder.objects.all())

        context = {"data": data, "form": AppForm, "doesNotExist": True}
        context["user"] = request.user

        return render(request, "verifyRestockOrder/verifyRO_table.html", context)


@login_required
def verifyRO_approved(request):
    restock_ID = request.POST["restockID"]
    selected_RO = RestockOrder.objects.get(restockID=restock_ID)

    selected_RO.status = Status.VERIFIED
    selected_RO.save()

    context = {
        "RO": selected_RO,
    }
    context["user"] = request.user

    return render(request, "verifyRestockOrder/verifyRO_approved.html", context)


@login_required
def verifyRO_disapproved(request):
    restock_ID = request.POST["restockID"]
    selected_RO = RestockOrder.objects.get(restockID=restock_ID)

    selected_RO.status = Status.DISAPPROVED
    selected_RO.save()

    context = {
        "RO": selected_RO,
    }
    context["user"] = request.user

    return render(request, "verifyRestockOrder/verifyRO_disapproved.html", context)
