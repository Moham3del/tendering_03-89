# Generated by Django 4.1.7 on 2023-03-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0046_contract_code_year_alter_contract_code_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract_detail',
            name='contract_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]