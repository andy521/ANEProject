# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0064_auto_20181017_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer771644', max_length=20, verbose_name='nickname'),
        ),
    ]
