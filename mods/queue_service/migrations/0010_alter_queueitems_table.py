# Generated by Django 3.2.9 on 2022-01-20 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queue_service', '0009_alter_queueitems_serial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='queueitems',
            table='mevrik_queue_items',
        ),
    ]
