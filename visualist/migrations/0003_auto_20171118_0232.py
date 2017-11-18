# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualist', '0002_source_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary'), ('work', 'work'), ('personal', 'personal')], default='primary', max_length=25)),
                ('address', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary'), ('work', 'work'), ('personal', 'personal')], default='primary', max_length=25)),
                ('country', models.IntegerField()),
                ('area_code', models.IntegerField()),
                ('exchange_code', models.IntegerField()),
                ('number', models.IntegerField()),
                ('extension', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('askfm', 'Ask.fm'), ('facebook', 'Facebook'), ('flickr', 'Flickr'), ('foursquare', 'Foursquare'), ('github', 'GitHub'), ('googleplus', 'Google+'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('meetup', 'Meetup'), ('pinterest', 'Pinterest'), ('reddit', 'Reddit'), ('snapchat', 'SnapChat'), ('tumblr', 'Tumblr'), ('twitter', 'Twitter'), ('vine', 'Vine'), ('whatsapp', 'WhatsApp'), ('yelp', 'Yelp'), ('youtube', 'YouTube')], default='primary', max_length=25)),
                ('account', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('href', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='source',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='source',
            name='same_as',
        ),
        migrations.AddField(
            model_name='source',
            name='same_as',
            field=models.ManyToManyField(blank=True, to='visualist.Website'),
        ),
    ]
