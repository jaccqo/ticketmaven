# Generated by Django 5.0.3 on 2024-03-27 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_userprofile_card_type_userprofile_expiry_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TicketPurchase',
            new_name='TeamsTicketPurchase',
        ),
    ]
