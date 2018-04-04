# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-04 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default=0, upload_to='image/%Y/%m'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='face_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
