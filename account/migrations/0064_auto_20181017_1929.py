# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0063_auto_20181017_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer852816', max_length=20, verbose_name='nickname'),
        ),
    ]