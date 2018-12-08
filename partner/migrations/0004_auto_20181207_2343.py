# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-12-07 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_auto_20181130_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='메뉴 이미지'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='메뉴 이름'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.PositiveIntegerField(verbose_name='가격'),
        ),
    ]
