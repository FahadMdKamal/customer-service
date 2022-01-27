# Generated by Django 3.2.9 on 2022-01-24 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_service', '0018_auto_20220124_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queueitems',
            name='status',
            field=models.CharField(choices=[('incative', 'Inactive'), ('attended', 'Attended'), ('pending', 'Pending'), ('closed', 'Closed'), ('unattended', 'Unattended'), ('disputed', 'Disputed')], default='pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='queueprinciples',
            name='last_active_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 13, 31, 46, 550316)),
        ),
    ]
