# Generated by Django 3.2.9 on 2021-11-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texonomy',
            name='texonomy_type',
            field=models.CharField(max_length=20),
        ),
    ]
