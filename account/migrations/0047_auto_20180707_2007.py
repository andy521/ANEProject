# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-07 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0046_auto_20180707_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer622527', max_length=20, verbose_name='nickname'),
        ),
    ]
