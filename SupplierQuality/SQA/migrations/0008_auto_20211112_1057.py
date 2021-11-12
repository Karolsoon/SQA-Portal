# Generated by Django 3.2.7 on 2021-11-12 09:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SQA', '0007_auto_20211112_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='number',
            field=models.CharField(default='8D YY/XXX', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='supplier_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='claim',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 11, 12, 9, 57, 7, 334780, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier_t1',
            name='valid_from',
            field=models.DateField(verbose_name=datetime.datetime(2021, 11, 12, 9, 57, 7, 332791, tzinfo=utc)),
        ),
    ]