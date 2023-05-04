from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import DeliveryOrder, PurchaseOrder, Item, Status
from app.forms import AppForm
from django.core import serializers

# Create your views here.


@login_required
def verifyDO_table(request):
    data = serializers.serialize("python", DeliveryOrder.objects.all())

    context = {
        "data": data,
        "form": AppForm,
    }
    context["user"] = request.user

    return render(request, "verifyDeliveryOrder/verifyDO_table.html", context)


@login_required
def verifyDO_compare(request):

    try:
        delivery_ID = request.POST["id"]
        selected_DO = DeliveryOrder.objects.get(deliveryID=delivery_ID)
        purchase_order_object = selected_DO.purchaseID
        data = serializers.serialize(
            "python", Item.objects.filter(purchaseID=purchase_order_object)
        )

        context = {
            "data": data,
            "DO": selected_DO,
            "PO": purchase_order_object,
        }
        context["user"] = request.user

        return render(request, "verifyDeliveryOrder/verifyDO_compare.html", context)

    except DeliveryOrder.DoesNotExist:
        data = serializers.serialize("python", DeliveryOrder.objects.all())

        context = {"data": data, "form": AppForm, "doesNotExist": True}
        context["user"] = request.user

        return render(request, "verifyDeliveryOrder/verifyDO_table.html", context)


@login_required
def verifyDO_approved(request):
    delivery_ID = request.POST["deliveryID"]
    selected_DO = DeliveryOrder.objects.get(deliveryID=delivery_ID)
    purchase_order_object = selected_DO.purchaseID
    data = serializers.serialize(
        "python", Item.objects.filter(purchaseID=purchase_order_object)
    )

    selected_DO.status = Status.VERIFIED
    selected_DO.save()

    context = {
        "data": data,
        "DO": selected_DO,
    }
    context["user"] = request.user

    return render(request, "verifyDeliveryOrder/verifyDO_approved.html", context)

@login_required
def verifyDO_disapproved(request):
    delivery_ID = request.POST["deliveryID"]
    selected_DO = DeliveryOrder.objects.get(deliveryID=delivery_ID)
    purchase_order_object = selected_DO.purchaseID
    data = serializers.serialize(
        "python", Item.objects.filter(purchaseID=purchase_order_object)
    )

    selected_DO.status = Status.DISAPPROVED
    selected_DO.save()

    context = {
        "data": data,
        "DO": selected_DO,
    }
    context["user"] = request.user

    return render(request, "verifyDeliveryOrder/verifyDO_disapproved.html", context)
