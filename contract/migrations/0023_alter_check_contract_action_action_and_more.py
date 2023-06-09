# Generated by Django 4.1.7 on 2023-03-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0022_alter_check_contract_action_action_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_contract_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract_detail',
            name='sgnlassign1_actionFile',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='contract_detail',
            name='sgnlassign2_actionFile',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='contract_detail',
            name='sgnlcheckContract_actionFile',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='contract_detail',
            name='sgnlcopyContract_actionFile',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
