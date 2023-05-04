from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import DeliveryOrder, PurchaseOrder, Item, RestockOrder
from app.forms import AppForm
from django.core import serializers


# Create your views here.


@login_required
def viewRO_table(request):
    data = serializers.serialize("python", RestockOrder.objects.all())

    context = {
        "title": "View Restock Order",
        "data": data,
        "form": AppForm,
    }
    context["user"] = request.user

    check_finance = request.user.groups.filter(name="finance department").exists()
    check_warehouse = request.user.groups.filter(name="warehouse department").exists()
    check_manager = request.user.groups.filter(name="manager").exists()

    if check_finance:
        return render(request, "viewRestockOrder/viewRO_table_finance.html", context)
    elif check_warehouse:
        return render(request, "viewRestockOrder/viewRO_table_warehouse.html", context)
    elif check_manager:
        return render(request, "viewRestockOrder/viewRO_table_manager.html", context)


@login_required
def viewRO_details(request):

    check_finance = request.user.groups.filter(name="finance department").exists()
    check_warehouse = request.user.groups.filter(name="warehouse department").exists()
    check_manager = request.user.groups.filter(name="manager").exists()

    try:
        restock_ID = request.POST["id"]
        selected_RO = RestockOrder.objects.get(restockID=restock_ID)

        context = {
            "RO": selected_RO,
        }
        context["user"] = request.user

        if check_finance:
            return render(
                request, "viewRestockOrder/viewRO_details_finance.html", context
            )
        elif check_warehouse:
            return render(
                request, "viewRestockOrder/viewRO_details_warehouse.html", context
            )
        elif check_manager:
            return render(
                request, "viewRestockOrder/viewRO_details_manager.html", context
            )

    except RestockOrder.DoesNotExist:
        data = serializers.serialize("python", RestockOrder.objects.all())

        context = {"data": data, "form": AppForm, "doesNotExist": True}
        context["user"] = request.user

        if check_finance:
            return render(
                request, "viewRestockOrder/viewRO_table_finance.html", context
            )
        elif check_warehouse:
            return render(
                request, "viewRestockOrder/viewRO_table_warehouse.html", context
            )
        elif check_manager:
            return render(
                request, "viewRestockOrder/viewRO_table_manager.html", context
            )
