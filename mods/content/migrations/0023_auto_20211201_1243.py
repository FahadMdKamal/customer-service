# Generated by Django 3.2.9 on 2021-12-01 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_content_app_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='flownode',
            name='content_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='flownode',
            name='initial_content_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.content'),
        ),
    ]
