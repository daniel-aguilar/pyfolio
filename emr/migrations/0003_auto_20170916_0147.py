# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0002_auto_20170915_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='identification',
            field=models.CharField(max_length=9, unique=True, verbose_name='Identification'),
        ),
    ]
