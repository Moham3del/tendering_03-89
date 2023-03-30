# Generated by Django 4.1.7 on 2023-03-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0012_alter_assignattach1_action_action_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlassign1_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlassign1_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlassign1_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlassign2_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlassign2_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlassign2_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlceo_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlceo_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlceo_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcheckContract_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcheckContract_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcheckContract_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcheckData_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcheckData_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcheckData_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcopyContract_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcopyContract_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcopyContract_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcostEstimation_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcostEstimation_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlcostEstimation_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlevp_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlevp_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlevp_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlfinancial_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlfinancial_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlfinancial_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlsectorManager_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlsectorManager_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnlsectorManager_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnltcta_action',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnltcta_action_creator',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contract_detail',
            name='sgnltcta_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]