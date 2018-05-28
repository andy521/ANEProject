# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 17:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0033_auto_20180511_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fans',
            name='fans',
        ),
        migrations.RemoveField(
            model_name='fans',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='owner',
        ),
        migrations.AddField(
            model_name='follow',
            name='fans',
            field=models.ForeignKey(default=2016301500226, on_delete=django.db.models.deletion.CASCADE, related_name='fans', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='WHUer887065', max_length=20, verbose_name='nickname'),
        ),
        migrations.DeleteModel(
            name='Fans',
        ),
    ]
