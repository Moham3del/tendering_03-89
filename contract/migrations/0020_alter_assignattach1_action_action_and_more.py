# Generated by Django 4.1.7 on 2023-03-15 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0019_alter_sector_manager_action_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignattach1_action',
            name='action',
            field=models.CharField(choices=[('تم', 'تم')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignattach1_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='assignattach2_action',
            name='action',
            field=models.CharField(choices=[('تم', 'تم')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignattach2_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='ceo_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ceo_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='check_contract_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='check_data_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='check_data_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='copy_contract_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='copy_contract_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='cost_estimation_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cost_estimation_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='evp_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evp_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='financial_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='financial_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
        migrations.AlterField(
            model_name='tcta_action',
            name='action',
            field=models.CharField(choices=[('قبول', 'قبول')], default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tcta_action',
            name='action_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract_detail'),
        ),
    ]
