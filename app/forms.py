"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from app.models import PurchaseOrder


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput({"class": "form-control", "placeholder": "User name"}),
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            {"class": "form-control", "placeholder": "Password"}
        ),
    )


class AppForm(forms.Form):
    deliveryAddress = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            {"class": "form-control", "placeholder": "Delivery Address"}
        ),
    )
    deliveryDate = forms.DateField(
        widget=forms.TextInput({"class": "form-control", "placeholder": "DD-MM-YYYY"})
    )
    itemID = forms.CharField(
        max_length=255,
        widget=forms.TextInput({"class": "form-control", "placeholder": "Item ID"}),
    )
    itemName = forms.CharField(
        max_length=255,
        widget=forms.TextInput({"class": "form-control", "placeholder": "Item Name"}),
    )
    itemQuantity = forms.IntegerField(widget=forms.widgets.NumberInput())
    unitPrice = forms.FloatField(widget=forms.widgets.NumberInput())
    id = forms.CharField(
        max_length=255, widget=forms.TextInput({"class": "form-control"})
    )


class PurchaseIDSelector(forms.ModelForm):
    purchaseID = forms.ModelChoiceField(queryset=PurchaseOrder.objects.all())

    class Meta:
        model = PurchaseOrder
        fields = ["purchaseID"]
