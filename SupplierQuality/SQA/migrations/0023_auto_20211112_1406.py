# Generated by Django 3.2.7 on 2021-11-12 13:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SQA', '0022_auto_20211112_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='ppap',
        ),
        migrations.AddField(
            model_name='ppap',
            name='part_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SQA.part'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 13, 6, 22, 898644, tzinfo=utc), verbose_name='Claim date'),
        ),
        migrations.AlterField(
            model_name='supplier_t1',
            name='valid_from',
            field=models.DateField(default=datetime.datetime(2021, 11, 12, 13, 6, 22, 895709, tzinfo=utc), verbose_name='Supplier validated on'),
        ),
    ]
