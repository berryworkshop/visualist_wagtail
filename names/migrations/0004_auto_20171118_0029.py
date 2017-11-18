# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 00:29
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0003_auto_20171118_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='employees',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='employers', to='names.Person'),
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='member_of', to='names.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='friends',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='_person_friends_+', to='names.Person'),
        ),
    ]
