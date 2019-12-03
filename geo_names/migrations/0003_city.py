# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.db.models import CASCADE


class Migration(migrations.Migration):

    dependencies = [
        ('geo_names', '0002_countryalternate'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=15, decimal_places=10)),
                ('timezone', models.CharField(max_length=255)),
                ('feature_class', models.CharField(max_length=1)),
                ('feature_code', models.CharField(max_length=10)),
                ('date_modification', models.CharField(max_length=255)),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('datetime_update', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='geo_names.Country', on_delete=CASCADE)),
            ],
        ),
    ]
