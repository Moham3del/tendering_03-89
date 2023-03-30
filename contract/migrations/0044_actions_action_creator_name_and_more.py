# Generated by Django 4.1.7 on 2023-03-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0043_contract_detail_creator_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='assignmnt_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ceo_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check_contract_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check_data_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlassignmnt_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlceo_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcheckContract_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcheckData_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcopyContract_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcostEstimation_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlevp_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlfinancial_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlsectorManager_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnltcta_action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='copy_contract_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cost_estimation_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evp_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financial_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sector_manager_action',
            name='action_creator_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='tcta_action',
            name='action_creator_name',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ceo_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول'), ('ملاحظات', 'ملاحظات'), ('رفض', 'رفض')], max_length=250),
        ),
        migrations.AlterField(
            model_name='evp_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول'), ('ملاحظات', 'ملاحظات'), ('رفض', 'رفض')], max_length=250),
        ),
        migrations.AlterField(
            model_name='tcta_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول'), ('ملاحظات', 'ملاحظات'), ('رفض', 'رفض')], max_length=250),
        ),
    ]
