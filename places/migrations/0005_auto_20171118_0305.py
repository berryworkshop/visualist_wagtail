# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualist', '0005_extraname'),
        ('places', '0004_auto_20171118_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='appointment_only',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='place',
            name='extra_names',
            field=models.ManyToManyField(blank=True, to='visualist.ExtraName'),
        ),
        migrations.AddField(
            model_name='place',
            name='group_friendly',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='place',
            name='hours',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
