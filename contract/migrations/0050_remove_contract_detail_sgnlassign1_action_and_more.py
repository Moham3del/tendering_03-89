# Generated by Django 4.1.7 on 2023-03-29 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0049_remove_assignmnt_action_contract_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract_detail',
            name='sgnlassign1_action',
        ),
        migrations.RemoveField(
            model_name='contract_detail',
            name='sgnlassign1_actionFile',
        ),
        migrations.RemoveField(
            model_name='contract_detail',
            name='sgnlassign1_action_creator',
        ),
        migrations.RemoveField(
            model_name='contract_detail',
            name='sgnlassign1_action_date',
        ),
    ]
