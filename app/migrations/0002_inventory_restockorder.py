# Generated by Django 4.1.4 on 2023-01-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inventory",
            fields=[
                ("inventoryID", models.AutoField(primary_key=True, serialize=False)),
                ("itemName", models.CharField(max_length=255)),
                ("itemQuantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RestockOrder",
            fields=[
                ("restockID", models.AutoField(primary_key=True, serialize=False)),
                ("itemName", models.CharField(max_length=255)),
                ("itemQuantity", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[("Pending", "Pending"), ("Verified", "Verified")],
                        default="Pending",
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]
