# Generated by Django 4.1.1 on 2023-01-27 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0007_t_detail_bid_opening_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_detail',
            name='remaining_time',
        ),
    ]