# Generated by Django 3.2.7 on 2021-11-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SQA', '0027_ppap_valid_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppap',
            name='is_valid',
            field=models.BooleanField(default=False, verbose_name='Part is validated'),
        ),
    ]
