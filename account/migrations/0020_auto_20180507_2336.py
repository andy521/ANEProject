# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20180502_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer593528', max_length=20, verbose_name='nickname'),
        ),
    ]
