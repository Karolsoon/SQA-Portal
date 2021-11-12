# Generated by Django 3.2.7 on 2021-11-12 09:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SQA', '0004_auto_20211111_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ppap',
            name='part',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SQA.part'),
        ),
        migrations.AlterField(
            model_name='supplier_t1',
            name='valid_from',
            field=models.DateField(verbose_name=datetime.datetime(2021, 11, 12, 9, 41, 1, 436597, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 11, 12, 9, 41, 1, 438588, tzinfo=utc))),
                ('closed', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('supplier_t1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SQA.supplier_t1')),
            ],
        ),
    ]