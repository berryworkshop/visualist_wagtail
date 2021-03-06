# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('events', '0001_initial'),
        ('visualist', '0001_initial'),
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizers',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='names.Agent'),
        ),
        migrations.AddField(
            model_name='event',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='visualist.Source'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='events.EventTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
