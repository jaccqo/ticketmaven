# Generated by Django 5.0.3 on 2024-03-24 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_automated',
            field=models.BooleanField(default=False),
        ),
    ]