# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0029_auto_20161009_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='fake',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='虚拟资金'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='section',
            field=models.CharField(blank=True, choices=[('1AgriculturalCommodities', '农产品'), ('2NonAgriculturalCommodities', '工业品'), ('3Equities', '股指'), ('4Rates', '利率'), ('5Currencies', '货币')], max_length=48, null=True, verbose_name='分类'),
        ),
    ]
