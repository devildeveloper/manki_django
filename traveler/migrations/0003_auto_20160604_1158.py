# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveler', '0002_auto_20160604_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='passwd',
            field=models.CharField(default='XXGXRA', max_length=12),
        ),
    ]