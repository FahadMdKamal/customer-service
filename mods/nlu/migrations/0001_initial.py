# Generated by Django 3.2.9 on 2022-02-08 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NluEntities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244, unique=True)),
                ('role', models.CharField(blank=True, max_length=244, null=True)),
                ('confidence_score', models.IntegerField(blank=True, null=True)),
                ('value', models.CharField(blank=True, max_length=244, null=True)),
                ('position', models.JSONField(blank=True, null=True)),
                ('value_parser', models.CharField(blank=True, max_length=244, null=True)),
                ('value_config', models.CharField(blank=True, max_length=244, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'nlu_entities',
            },
        ),
        migrations.CreateModel(
            name='NluIntent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244, unique=True)),
                ('short_code', models.CharField(max_length=244, unique=True)),
                ('marked', models.CharField(choices=[('Favourite', 'Favourite'), ('Like', 'Like')], default='Favourite', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'nlu_intent',
            },
        ),
        migrations.CreateModel(
            name='NluSync',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(max_length=244)),
                ('owner_id', models.CharField(blank=True, default='wit', max_length=244, null=True)),
                ('owner_type', models.CharField(choices=[('intent', 'intent'), ('entities', 'entities'), ('traits', 'traits'), ('utterances', 'utterances')], max_length=50, null=True)),
                ('property_request', models.JSONField(blank=True, null=True)),
                ('property_response', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(max_length=244)),
                ('request_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'nlu_sync',
            },
        ),
        migrations.CreateModel(
            name='StaticDictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_type', models.CharField(max_length=244)),
                ('term_context', models.CharField(blank=True, max_length=244, null=True)),
                ('term_value', models.CharField(max_length=244)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'nlu_static_dictionary',
            },
        ),
        migrations.CreateModel(
            name='NluUtterances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('intent_confidence', models.FloatField(default=0.0)),
                ('sentence', models.CharField(max_length=244)),
                ('entities', models.JSONField()),
                ('traits', models.JSONField()),
                ('comment', models.CharField(blank=True, max_length=244, null=True)),
                ('status', models.CharField(max_length=244)),
                ('trained', models.IntegerField(default=0)),
                ('weight', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nlu.nluintent')),
            ],
            options={
                'db_table': 'nlu_utterances',
            },
        ),
        migrations.AddField(
            model_name='nluintent',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nlu.staticdictionary'),
        ),
        migrations.CreateModel(
            name='NluImportFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utterances', models.CharField(max_length=244)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('intent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nlu.nluintent')),
            ],
            options={
                'db_table': 'nlu_import_file',
            },
        ),
    ]
