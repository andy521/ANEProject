# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20180423_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer40805', max_length=20, verbose_name='nickname'),
        ),
        migrations.AlterModelTable(
            name='loginuser',
            table='LoginUser',
        ),
    ]
