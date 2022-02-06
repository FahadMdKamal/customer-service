# Generated by Django 3.2.9 on 2022-02-03 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QueueItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField()),
                ('topic', models.SlugField(choices=[('social', 'Social'), ('email', 'Email'), ('live_chat', 'Live_Chat'), ('live_call', 'Live_Call'), ('support', 'Support')], default='social', max_length=40)),
                ('serial', models.CharField(max_length=20)),
                ('source_ref', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('principle_id', models.IntegerField(default=0)),
                ('queue_variant', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('item_subject', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('item_from_ref', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('item_to_ref', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('priority', models.CharField(default='normal', max_length=100)),
                ('status', models.CharField(choices=[('incative', 'Inactive'), ('attended', 'Attended'), ('pending', 'Pending'), ('closed', 'Closed'), ('unattended', 'Unattended'), ('disputed', 'Disputed')], default='pending', max_length=100)),
                ('metadata', models.JSONField(default=dict)),
                ('escalation_timeout', models.IntegerField(default=0)),
                ('dispute_timeout', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'mevrik_queue_items',
            },
        ),
        migrations.CreateModel(
            name='QueuePrinciples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principle_type', models.CharField(choices=[('user', 'User'), ('workgroup', 'Workgroup')], default='user', max_length=20)),
                ('principle_id', models.IntegerField(unique=True)),
                ('display_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('online', models.CharField(choices=[('agent_present', 'AGENT_PRESENT'), ('agent_not_present', 'AGENT_NOT_PRESENT')], default='agent_not_present', max_length=30)),
                ('last_assigned_at', models.DateTimeField(blank=True, null=True)),
                ('principle_meta', models.JSONField(default=dict)),
            ],
            options={
                'db_table': 'mevrik_queue_principles',
            },
        ),
        migrations.CreateModel(
            name='QueueTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField()),
                ('topic', models.SlugField(choices=[('social', 'Social'), ('email', 'Email'), ('live_chat', 'Live_Chat'), ('live_call', 'Live_Call'), ('support', 'Support')], default='social', max_length=40)),
                ('allowed_source', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('push_direction', models.CharField(blank=True, choices=[('fifo', 'FIFO'), ('lifo', 'LIFO')], default='fifo', max_length=20, null=True)),
                ('escalation_timeout', models.IntegerField(blank=True, default=0)),
                ('dispute_timeout', models.IntegerField(blank=True, default=0)),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('paused', 'PAUSED'), ('closed', 'CLOSED'), ('retired', 'RETIRED')], default='open', max_length=20)),
                ('last_open_at', models.DateTimeField(blank=True, null=True)),
                ('last_closed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'mevrik_queue_topics',
            },
        ),
        migrations.CreateModel(
            name='HistoricalQueuePrinciples',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('principle_type', models.CharField(choices=[('user', 'User'), ('workgroup', 'Workgroup')], default='user', max_length=20)),
                ('principle_id', models.IntegerField(db_index=True)),
                ('display_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('online', models.CharField(choices=[('agent_present', 'AGENT_PRESENT'), ('agent_not_present', 'AGENT_NOT_PRESENT')], default='agent_not_present', max_length=30)),
                ('last_assigned_at', models.DateTimeField(blank=True, null=True)),
                ('principle_meta', models.JSONField(default=dict)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical queue principles',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalQueueItems',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('app_id', models.IntegerField()),
                ('topic', models.SlugField(choices=[('social', 'Social'), ('email', 'Email'), ('live_chat', 'Live_Chat'), ('live_call', 'Live_Call'), ('support', 'Support')], default='social', max_length=40)),
                ('serial', models.CharField(max_length=20)),
                ('source_ref', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('principle_id', models.IntegerField(default=0)),
                ('queue_variant', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('item_subject', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('item_from_ref', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('item_to_ref', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('priority', models.CharField(default='normal', max_length=100)),
                ('status', models.CharField(choices=[('incative', 'Inactive'), ('attended', 'Attended'), ('pending', 'Pending'), ('closed', 'Closed'), ('unattended', 'Unattended'), ('disputed', 'Disputed')], default='pending', max_length=100)),
                ('metadata', models.JSONField(default=dict)),
                ('escalation_timeout', models.IntegerField(default=0)),
                ('dispute_timeout', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical queue items',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
