# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0050_auto_20180708_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer97760', max_length=20, verbose_name='nickname'),
        ),
    ]