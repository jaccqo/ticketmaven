# Generated by Django 5.0.3 on 2024-03-28 01:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_ticketpurchase_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketpurchase',
            name='purchase_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
