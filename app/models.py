"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

#sharing entity

class PurchaseOrder(models.Model):
    purchaseID      = models.AutoField(primary_key=True)
    deliveryAddress = models.CharField(null=False, max_length=255)
    deliveryDate    = models.CharField(null=False, max_length=15)
    clientName      = models.CharField(null=False, max_length=255)
    totalPrice      = models.FloatField(null=True)

class Item(models.Model):
    itemID       = models.AutoField(primary_key=True)
    itemName     = models.CharField(null=False, max_length=255)
    itemQuantity = models.IntegerField(null=False)
    unitPrice    = models.FloatField(null=False)
    purchaseID   = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True)

class Status(models.TextChoices):
    PENDING  = "Pending"
    VERIFIED = "Verified"
    DISAPPROVED = "Disapproved"

class DeliveryOrder(models.Model):
    deliveryID      = models.AutoField(primary_key=True)
    purchaseID      = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE)
    deliveryAddress = models.CharField(null=False, max_length=255)
    deliveryDate    = models.CharField(null=False, max_length=15)
    status          = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=15)

class RestockOrder(models.Model):
    restockID    = models.AutoField(primary_key=True)
    itemName     = models.CharField(null=False, max_length=255)
    itemQuantity = models.IntegerField(null=False)
    status       = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=15)

class Inventory(models.Model):
    inventoryID  = models.AutoField(primary_key=True)
    itemName     = models.CharField(null=False, max_length=255)
    itemQuantity = models.IntegerField(null=False)

