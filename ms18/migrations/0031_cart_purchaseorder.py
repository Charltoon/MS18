# Generated by Django 4.2.6 on 2024-01-16 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ms18', '0030_remove_requisition_requestedproduct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='PurchaseOrder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ms18.purchaseorder'),
        ),
    ]