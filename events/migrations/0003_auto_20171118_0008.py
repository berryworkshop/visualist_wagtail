# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 00:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20171117_2315'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('start_date', 'duration', 'precision')]),
        ),
    ]
