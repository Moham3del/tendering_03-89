# Generated by Django 4.1.7 on 2023-03-08 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0009_alter_sector_manager_action_action_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector_manager_action',
            name='action_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
