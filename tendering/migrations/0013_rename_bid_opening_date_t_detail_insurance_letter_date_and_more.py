# Generated by Django 4.1.1 on 2023-01-30 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0012_alter_t_detail_management_alter_t_detail_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_detail',
            old_name='Bid_opening_date',
            new_name='insurance_letter_date',
        ),
        migrations.RenameField(
            model_name='t_detail',
            old_name='publication_date',
            new_name='starting_date',
        ),
        migrations.RemoveField(
            model_name='t_detail',
            name='documents_value',
        ),
        migrations.RemoveField(
            model_name='t_detail',
            name='includes_supplyitems',
        ),
    ]