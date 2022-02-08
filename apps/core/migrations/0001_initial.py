# Generated by Django 3.2.9 on 2022-02-08 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=255, unique=True)),
                ('app_code', models.CharField(max_length=20, unique=True)),
                ('app_domain', models.CharField(blank=True, max_length=255, null=True)),
                ('app_config', models.JSONField(blank=True, default=dict, null=True)),
                ('app_icon', models.CharField(blank=True, max_length=20, null=True)),
                ('allowed_domains', models.JSONField(blank=True, default=dict, null=True)),
                ('allowed_channel_types', models.CharField(choices=[('facebook', 'Facebook'), ('whatsapp', 'WhatsApp'), ('email', 'Email')], default='facebook', max_length=10)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Mavrik Apps',
                'db_table': 'core_apps',
            },
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAllowOrigin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(blank=True, max_length=50, null=True)),
                ('principal', models.CharField(choices=[('apikey', 'API Key'), ('username', 'User Name')], default='user', max_length=15)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('origin_type', models.CharField(choices=[('referrer', 'Referrer'), ('cidr', 'CIDR'), ('cookie', 'Cookie')], default='cidr', max_length=15)),
                ('origin_sig', models.CharField(blank=True, default='0.0.0.0', max_length=20, null=True)),
                ('expire_at', models.DateTimeField(blank=True, null=True)),
                ('allowed', models.BooleanField(default=False)),
                ('last_seen_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_user_allowed_origins',
            },
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
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('login_attempts', models.IntegerField(default=0)),
                ('allowed_apps', models.ManyToManyField(blank=True, related_name='user_apps', to='core.Apps')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_user_profiles',
            },
        ),
        migrations.CreateModel(
            name='PasswordStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashed_pass', models.CharField(max_length=255)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_passwords_store',
            },
        ),
        migrations.CreateModel(
            name='LoggedInUserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(max_length=50)),
                ('browser', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=40)),
                ('hash', models.CharField(max_length=255)),
                ('is_allowed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logged_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=100)),
                ('channel_ref', models.CharField(blank=True, max_length=20, null=True)),
                ('channel_type', models.CharField(choices=[('facebook_page', 'Facebook Page'), ('facebook_messenger', 'Facebook Messenger'), ('live_chat', 'Live Chat'), ('whatsapp', 'WhatsApp'), ('API', 'API'), ('email', 'Email')], max_length=40)),
                ('details', models.JSONField(blank=True, default=dict, null=True)),
                ('config', models.JSONField(blank=True, default=dict, null=True)),
                ('status', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=True)),
                ('connectivity_status', models.CharField(choices=[('active', 'Active'), ('expired', 'Expire'), ('paused', 'Paused'), ('retired', 'Retired'), ('unused', 'Unused'), ('inactive', 'Inactive')], default=True, max_length=15)),
                ('connectivity_note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.apps')),
                ('mail_box', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel_mail_box', to='core.mailbox')),
            ],
            options={
                'verbose_name_plural': 'Marik Channels',
                'db_table': 'core_channel',
                'unique_together': {('app', 'channel_name')},
            },
        ),
        migrations.CreateModel(
            name='WorkGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.CharField(blank=True, choices=[('admin', 'Admin'), ('manager', 'Manager'), ('supervisor', 'Supervisor')], default='admin', max_length=50, null=True)),
                ('name', models.CharField(max_length=255)),
                ('permissions', models.JSONField(blank=True, null=True)),
                ('active_since', models.DateTimeField(blank=True, null=True)),
                ('user_workgroups', models.JSONField(blank=True, null=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.channels')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Work Groups',
                'db_table': 'core_work_group',
                'unique_together': {('channel', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxonomy_type', models.CharField(max_length=50)),
                ('context', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('crumbs', models.CharField(blank=True, max_length=255, null=True)),
                ('ref_path', models.CharField(blank=True, max_length=255, null=True)),
                ('display_order', models.IntegerField(default=0)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('details', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.channels')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.taxonomy')),
            ],
            options={
                'db_table': 'core_taxonomy',
                'unique_together': {('app_id', 'taxonomy_type', 'name')},
            },
        ),
    ]