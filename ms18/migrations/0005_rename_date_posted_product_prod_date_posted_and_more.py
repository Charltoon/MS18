# Generated by Django 4.2.6 on 2024-01-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms18', '0004_purchaseorder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date_posted',
            new_name='PROD_DATE_POSTED',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='content',
            new_name='PROD_DESCRIPTION',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='PROD_IMAGE',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='PROD_NAME',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='date_posted',
            new_name='ORD_DATE_POSTED',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='content',
            new_name='ORD_DESCRIPTION',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='employee',
            new_name='ORD_EMPLOYEE',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='title',
            new_name='ORD_NAME',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='quantity',
            new_name='ORD_QUANTITY',
        ),
        migrations.RemoveField(
            model_name='product',
            name='employee',
        ),
        migrations.AddField(
            model_name='product',
            name='PROD_PRICE',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='PROD_QUANTITY',
            field=models.IntegerField(default=0),
        ),
    ]