# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('capital', models.CharField(max_length=255)),
                ('geoname_id', models.PositiveIntegerField()),
                ('iso', models.CharField(max_length=2)),
                ('iso3', models.CharField(max_length=3)),
                ('iso_numeric', models.CharField(max_length=3)),
                ('fips', models.CharField(max_length=3)),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('datetime_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
