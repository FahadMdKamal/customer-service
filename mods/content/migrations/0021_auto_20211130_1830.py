# Generated by Django 3.2.9 on 2021-11-30 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0020_auto_20211129_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentmedia',
            old_name='public_url',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='contentmedia',
            name='media_ref',
            field=models.CharField(default='media/', max_length=244),
        ),
        migrations.AlterField(
            model_name='contentmedia',
            name='media_type',
            field=models.CharField(default='image', max_length=100),
        ),
        migrations.AlterField(
            model_name='contentmedia',
            name='status',
            field=models.CharField(default='active', max_length=244),
        ),
        migrations.AlterField(
            model_name='contentmedia',
            name='storage_provider',
            field=models.CharField(default='local', max_length=100),
        ),
        migrations.AlterField(
            model_name='nodeconfig',
            name='flow_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='config', to='content.flownode'),
        ),
        migrations.AlterField(
            model_name='nodeconfig',
            name='value',
            field=models.JSONField(default={}),
        ),
    ]