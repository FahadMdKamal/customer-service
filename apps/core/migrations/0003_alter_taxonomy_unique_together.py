# Generated by Django 3.2.9 on 2022-02-06 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_taxonomy_app_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='taxonomy',
            unique_together={('app_id', 'taxonomy_type', 'name')},
        ),
    ]
