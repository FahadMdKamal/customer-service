# Generated by Django 3.2.9 on 2021-11-24 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_flownode_nodeconfig_nodecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='flownode',
            name='node_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='flownode',
            name='flow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flownodes', to='content.flow'),
        ),
        migrations.AlterField(
            model_name='flownode',
            name='name',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='nodeconfig',
            name='flow_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodeconfigs', to='content.flownode'),
        ),
    ]