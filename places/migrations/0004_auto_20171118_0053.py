# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_place_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='place',
            name='is_primary',
            field=models.BooleanField(default=False),
        ),
    ]