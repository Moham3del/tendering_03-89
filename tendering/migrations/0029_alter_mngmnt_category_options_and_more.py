# Generated by Django 4.1.7 on 2023-03-06 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0028_remove_task_task_user_task_task_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mngmnt_category',
            options={'ordering': ['name'], 'verbose_name': 'Management'},
        ),
        migrations.AlterModelOptions(
            name='owner_list',
            options={'ordering': ['name'], 'verbose_name': 'owner'},
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
