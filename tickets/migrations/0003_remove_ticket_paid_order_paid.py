# Generated by Django 5.2.1 on 2025-05-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_order_id_alter_ticket_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
