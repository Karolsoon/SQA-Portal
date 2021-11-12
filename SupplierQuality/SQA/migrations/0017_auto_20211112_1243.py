# Generated by Django 3.2.7 on 2021-11-12 11:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SQA', '0016_auto_20211112_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='revision',
        ),
        migrations.RemoveField(
            model_name='ppap',
            name='part',
        ),
        migrations.AddField(
            model_name='part',
            name='ppap',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SQA.ppap'),
        ),
        migrations.AddField(
            model_name='ppap',
            name='revision',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='claim',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 11, 43, 33, 896948, tzinfo=utc), verbose_name='Claim date'),
        ),
        migrations.AlterField(
            model_name='supplier_t1',
            name='valid_from',
            field=models.DateField(default=datetime.datetime(2021, 11, 12, 11, 43, 33, 894823, tzinfo=utc), verbose_name='Supplier validated on'),
        ),
    ]