# Generated by Django 3.2.7 on 2021-11-12 11:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SQA', '0018_auto_20211112_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='is_produced',
        ),
        migrations.RemoveField(
            model_name='part',
            name='is_valid',
        ),
        migrations.RemoveField(
            model_name='part',
            name='valid_from',
        ),
        migrations.AddField(
            model_name='ppap',
            name='is_produced',
            field=models.BooleanField(default=False, verbose_name='Is in production'),
        ),
        migrations.AddField(
            model_name='ppap',
            name='is_valid',
            field=models.BooleanField(default=False, verbose_name='Part is validated'),
        ),
        migrations.AddField(
            model_name='ppap',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='validation date'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 11, 59, 33, 88103, tzinfo=utc), verbose_name='Claim date'),
        ),
        migrations.AlterField(
            model_name='supplier_t1',
            name='valid_from',
            field=models.DateField(default=datetime.datetime(2021, 11, 12, 11, 59, 33, 86083, tzinfo=utc), verbose_name='Supplier validated on'),
        ),
    ]
