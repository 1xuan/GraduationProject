# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-02 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0003_auto_20180404_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='time',
            field=models.CharField(max_length=50, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]