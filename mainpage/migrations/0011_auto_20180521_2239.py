# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import mainpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_auto_20180521_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to=mainpage.models.get_book_upload_to, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(default='moren.jpg', upload_to=mainpage.models.get_food_upload_to, verbose_name='images'),
        ),
    ]