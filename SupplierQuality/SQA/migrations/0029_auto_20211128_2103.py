# Generated by Django 3.2.7 on 2021-11-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SQA', '0028_ppap_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='D3_closed_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='D3 closed on'),
        ),
        migrations.AddField(
            model_name='claim',
            name='D3_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='D6_closed_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='D6 closed on'),
        ),
        migrations.AddField(
            model_name='claim',
            name='D6_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='D8_closed_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='D8 closed on'),
        ),
        migrations.AddField(
            model_name='claim',
            name='D8_open',
            field=models.BooleanField(default=True),
        ),
    ]
