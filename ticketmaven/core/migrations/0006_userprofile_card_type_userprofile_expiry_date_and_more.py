# Generated by Django 5.0.3 on 2024-03-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ticketpurchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='card_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='expiry_date',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='expiry_year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
