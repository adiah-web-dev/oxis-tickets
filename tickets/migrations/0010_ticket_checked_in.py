# Generated by Django 5.2.1 on 2025-05-29 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_alter_ticket_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='checked_in',
            field=models.BooleanField(default=False),
        ),
    ]
