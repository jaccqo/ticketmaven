# Generated by Django 5.0.3 on 2024-03-27 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_monthlyticketpurchase_projection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketpurchase',
            name='purchase_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 21, 29, 4, 691503)),
        ),
    ]