# Generated by Django 3.2.7 on 2021-11-12 11:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SQA', '0012_auto_20211112_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='closed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='claim',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 11, 12, 11, 13, 53, 973366, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='part',
            name='is_produced',
            field=models.BooleanField(default=False, verbose_name='Is in production'),
        ),
        migrations.AlterField(
            model_name='part',
            name='is_valid',
            field=models.BooleanField(default=False, verbose_name='Part is validated'),
        ),
        migrations.AlterField(
            model_name='part',
            name='subassy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SQA.subassembly'),
        ),
        migrations.AlterField(
            model_name='supplier_t1',
            name='valid_from',
            field=models.DateField(verbose_name=datetime.datetime(2021, 11, 12, 11, 13, 53, 970219, tzinfo=utc)),
        ),
    ]
