# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveler', '0003_auto_20160604_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your Name', max_length=200)),
                ('email', models.EmailField(help_text='Your Email', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='schema',
            name='passwd',
            field=models.CharField(default='2Q9ETR', max_length=12),
        ),
    ]
