# Generated by Django 3.2.9 on 2022-01-18 20:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_useralloworigin_expire_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useralloworigin',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 20, 14, 18, 794732)),
        ),
    ]
