# Generated by Django 3.2.7 on 2021-11-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_contentcustomfields_contentvars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversecontenttype',
            name='config_keys',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conversecontenttype',
            name='params',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
