# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 00:12
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='places.PlaceCategory'),
        ),
    ]
