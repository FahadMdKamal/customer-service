# Generated by Django 3.2.9 on 2022-01-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_service', '0008_alter_queueitems_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queueitems',
            name='serial',
            field=models.CharField(max_length=20),
        ),
    ]
