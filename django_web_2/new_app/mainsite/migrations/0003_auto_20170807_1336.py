# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='location default', max_length=120),
        ),
    ]
