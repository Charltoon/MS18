# Generated by Django 5.0.1 on 2024-01-12 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms18', '0015_remove_requestedproduct_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisition',
            old_name='REQ_EMPLOYEE',
            new_name='REQ_NAME',
        ),
        migrations.AddField(
            model_name='requisition',
            name='REQ_DESCRIPTION',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='requisition',
            name='REQ_QUANTITY',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
