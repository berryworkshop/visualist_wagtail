# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('authors', models.CharField(blank=True, max_length=250, null=True)),
                ('editors', models.CharField(blank=True, max_length=250, null=True)),
                ('translators', models.CharField(blank=True, max_length=250, null=True)),
                ('identifiers', models.CharField(blank=True, max_length=250, null=True)),
                ('archive', models.CharField(blank=True, max_length=250, null=True)),
                ('edition', models.CharField(blank=True, max_length=250, null=True)),
                ('pages', models.CharField(blank=True, max_length=250, null=True)),
                ('volume', models.CharField(blank=True, max_length=250, null=True)),
                ('series', models.CharField(blank=True, max_length=250, null=True)),
                ('same_as', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
