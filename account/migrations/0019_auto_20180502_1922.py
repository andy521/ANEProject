# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20180502_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer510509', max_length=20, verbose_name='nickname'),
        ),
    ]
