# Generated by Django 3.2.9 on 2021-11-23 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_alter_flow_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('flow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.flow')),
            ],
            options={
                'db_table': 'content_flow_node',
            },
        ),
        migrations.CreateModel(
            name='NodeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.content')),
                ('flow_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.flownode')),
            ],
            options={
                'db_table': 'content_node_contents',
            },
        ),
        migrations.CreateModel(
            name='NodeConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=244)),
                ('value', models.CharField(max_length=244)),
                ('flow_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.flownode')),
            ],
            options={
                'db_table': 'content_node_config',
            },
        ),
    ]