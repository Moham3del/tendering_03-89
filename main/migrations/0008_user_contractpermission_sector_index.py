# Generated by Django 4.1.7 on 2023-03-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_user_index_user_contractpermission_project_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_contractpermission',
            name='sector_index',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('NO', 'No')], max_length=250, null=True),
        ),
    ]
