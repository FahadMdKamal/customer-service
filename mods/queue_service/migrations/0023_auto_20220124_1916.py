# Generated by Django 3.2.9 on 2022-01-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_service', '0022_auto_20220124_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalqueueprinciples',
            name='last_active_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalqueueprinciples',
            name='last_assigned_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='queueprinciples',
            name='last_active_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='queueprinciples',
            name='last_assigned_at',
            field=models.DateTimeField(),
        ),
    ]
