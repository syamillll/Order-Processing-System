"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app import views as main_views
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime


# Client
from submitPurchaseOrder import views as submitPO_views
from viewDeliveryOrder import views as viewDO_views

# Finance
from viewPurchaseOrder import views as viewPO_views
from createDeliveryOrder import views as createDO_views

# Warehouse
from submitRestockOrder import views as submitRO_views
from viewInventory import views as viewInventory_views
from confirmItemAvailability import views as confirmItem_views

# Manager
from viewAllDeliveryOrder import views as viewAllDO_views
from verifyDeliveryOrder import views as verifyDO_views
from viewRestockOrder import views as viewRO_views
from verifyRestockOrder import views as verifyRO_views


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$', 
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^login$', 
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/logout.html'),
        name='logout'),
    re_path(r'^menu$', main_views.menu, name='menu'),

    re_path(r'^submitPO$', submitPO_views.submitPO, name='submitPO'),
    re_path(r'^submitPOform$', submitPO_views.submitPO_form, name='submitPO_form'),
    re_path(r'^submitPOitems$', submitPO_views.submitPO_items, name='submitPO_items'),

    re_path(r'^viewPO$', viewPO_views.viewPO_table, name='viewPO'),
    re_path(r'^viewPOdetails$', viewPO_views.viewPO_details, name='viewPO_details'),

    re_path(r'^createDO$', createDO_views.createDO_form, name='createDO_form'),
    re_path(r'^createDOitems$', createDO_views.createDO_item, name='createDO_items'),

    re_path(r'^viewDO$', viewDO_views.viewDO_table, name='viewPO'),
    re_path(r'^viewDOdetails$', viewDO_views.viewDO_details, name='viewDO_details'),

    re_path(r'^viewAllDO$', viewAllDO_views.viewAllDO_table, name='viewPO'),
    re_path(r'^viewAllDOdetails$', viewAllDO_views.viewAllDO_details, name='viewAllDO_details'),
    
    re_path(r'^verifyDO$', verifyDO_views.verifyDO_table, name='viewDO'),
    re_path(r'^verifyDOcompare$', verifyDO_views.verifyDO_compare, name='viewDO_compare'),
    re_path(r'^verifyDOapproved$', verifyDO_views.verifyDO_approved, name='viewDO_approved'),
    re_path(r'^verifyDOdisapproved$', verifyDO_views.verifyDO_disapproved, name='viewDO_disapproved'),

    re_path(r'^submitRO$', submitRO_views.submitRO, name='submitRO'),
    re_path(r'^submitROsuccess$', submitRO_views.submitRO_success, name='submitRO_sucesss'),

    re_path(r'^viewRO$', viewRO_views.viewRO_table, name='viewRO'),
    re_path(r'^viewROdetails$', viewRO_views.viewRO_details, name='viewRO_details'),

    re_path(r'^verifyRO$', verifyRO_views.verifyRO, name='verifyRO'),
    re_path(r'^verifyROcompare$', verifyRO_views.verifyRO_compare, name='verifyRO_compare'),
    re_path(r'^verifyROapproved$', verifyRO_views.verifyRO_approved, name='verifyRO_approved'),
    re_path(r'^verifyROdisapproved$', verifyRO_views.verifyRO_disapproved, name='verifyRO_disapproved'),

    re_path(r'^viewInventory$', viewInventory_views.viewInventory, name='viewInventory'),
    re_path(r'^confirmItem$', confirmItem_views.confirmItem, name='confirmItem'),



]
