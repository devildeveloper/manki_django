# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveler', '0004_auto_20160606_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='passwd',
            field=models.CharField(default='7EBN2U', max_length=12),
        ),
    ]
