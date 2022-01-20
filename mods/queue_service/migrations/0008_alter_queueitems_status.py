# Generated by Django 3.2.9 on 2022-01-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_service', '0007_queueitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queueitems',
            name='status',
            field=models.CharField(choices=[('incative', 'Inactive'), ('pending', 'Pending'), ('closed', 'Closed'), ('unattended', 'Unattended'), ('disputed', 'Disputed')], default='pending', max_length=100),
        ),
    ]
