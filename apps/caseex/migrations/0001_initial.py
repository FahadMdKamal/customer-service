# Generated by Django 3.2.9 on 2021-12-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(default=0)),
                ('source_ref', models.IntegerField(default=0)),
                ('ref_id', models.CharField(help_text='auto generated with app_id,date,shot_uuid', max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('group_id', models.IntegerField(default=0)),
                ('metadata', models.JSONField(default=dict)),
                ('status', models.CharField(choices=[('new', 'New'), ('open', 'Open'), ('hold', 'Hold'), ('closed', 'Closed'), ('escalated', 'Escalated')], default='new', max_length=20)),
                ('options', models.CharField(choices=[('allow_attachments', 'Allow Attachments'), ('allow_threaded_replies', 'Allow Threaded Replies'), ('closed_replay', 'Closed Replay')], default='allow_attachments', max_length=50)),
                ('case_tags', models.CharField(blank=True, max_length=20, null=True)),
                ('case_priority', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], default='low', max_length=20)),
                ('case_type', models.CharField(choices=[('support', 'Support'), ('problem', 'Problem'), ('incident', 'Incident'), ('question', 'Question'), ('task', 'Task')], default='support', max_length=20)),
                ('case_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'caseex_CaseId',
            },
        ),
    ]
