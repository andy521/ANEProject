# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_auto_20180509_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer680463', max_length=20, verbose_name='nickname'),
        ),
    ]
