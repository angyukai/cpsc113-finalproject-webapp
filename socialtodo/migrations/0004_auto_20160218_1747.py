# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialtodo', '0003_auto_20160218_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='collab1',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='collab2',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='collab3',
            field=models.EmailField(max_length=50),
        ),
    ]
