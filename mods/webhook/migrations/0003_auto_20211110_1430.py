# Generated by Django 3.2.9 on 2021-11-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0002_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ticket',
            name='body_parsed',
            field=models.TextField(default=''),
        ),
    ]