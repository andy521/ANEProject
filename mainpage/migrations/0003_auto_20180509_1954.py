# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20180509_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcomment',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mainpage.Food'),
        ),
    ]