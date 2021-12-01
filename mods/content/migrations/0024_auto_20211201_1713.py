# Generated by Django 3.2.9 on 2021-12-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0023_auto_20211201_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagetemplate',
            name='attachment',
        ),
        migrations.RemoveField(
            model_name='messagetemplate',
            name='template_var',
        ),
        migrations.AddField(
            model_name='messagetemplate',
            name='attachments',
            field=models.JSONField(default=dict, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='messagetemplate',
            name='name',
            field=models.CharField(default='Initial', max_length=244),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messagetemplate',
            name='template_vars',
            field=models.JSONField(default=dict, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='allowed_channel_types',
            field=models.JSONField(default=dict, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'In Active'), ('draft', 'Draft')], default='active', max_length=15),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='template_format',
            field=models.CharField(choices=[('text', 'Text'), ('markdown', 'Markdown'), ('mustache', 'Mustache')], default='text', max_length=15),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='template_group_id',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='template_type',
            field=models.CharField(choices=[('message', 'Message'), ('email', 'Email')], default='message', max_length=15),
        ),
    ]