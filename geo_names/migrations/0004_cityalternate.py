# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.db.models import CASCADE


class Migration(migrations.Migration):

    dependencies = [
        ('geo_names', '0003_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityAlternate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('iso_language', models.CharField(max_length=3)),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('datetime_update', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(to='geo_names.City', on_delete=CASCADE)),
            ],
        ),
    ]
