# Generated by Django 5.0.3 on 2024-03-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_team_password_team_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
