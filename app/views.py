# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def menu(request):
    check_client = request.user.groups.filter(name="client").exists()
    check_finance = request.user.groups.filter(name="finance department").exists()
    check_warehouse = request.user.groups.filter(name="warehouse department").exists()
    check_manager = request.user.groups.filter(name="manager").exists()

    # Client Home
    if check_client:
        context = {
            "title": "Home",
            "is_client": check_client,
            "year": datetime.now().year,
        }
        context["user"] = request.user
        return render(request, "app/client_homepage.html", context)

    # Finance Department Home
    elif check_finance:
        context = {
            "title": "Home",
            "is_finance": check_finance,
            "year": datetime.now().year,
        }
        context["user"] = request.user
        return render(request, "app/finance_homepage.html", context)

    # Warehouse Department Home
    elif check_warehouse:
        context = {
            "title": "Home",
            "is_warehouse": check_warehouse,
            "year": datetime.now().year,
        }
        context["user"] = request.user
        return render(request, "app/warehouse_homepage.html", context)

    # Manager Home
    elif check_manager:
        context = {
            "title": "Home",
            "is_manager": check_manager,
            "year": datetime.now().year,
        }
        context["user"] = request.user
        return render(request, "app/manager_homepage.html", context)
