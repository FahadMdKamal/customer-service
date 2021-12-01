# Generated by Django 3.2.9 on 2021-12-01 14:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211129_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxonomy',
            name='app_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='context',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='crumbs',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='photo_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='ref_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='taxonomy',
            name='taxonomy_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='taxonomy',
            unique_together={('taxonomy_type', 'name')},
        ),
        migrations.AlterModelTable(
            name='taxonomy',
            table='core_taxonomy',
        ),
        migrations.CreateModel(
            name='TaxonomyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(blank=True, max_length=255, null=True)),
                ('app_id', models.CharField(blank=True, max_length=255, null=True)),
                ('taxonomy_type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('details', models.CharField(choices=[('DESCRIPTION', 'Description'), ('PLURAL', 'plural')], default='DESCRIPTION', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.taxonomytype')),
            ],
            options={
                'db_table': 'core_taxonomy_type',
            },
        ),
    ]