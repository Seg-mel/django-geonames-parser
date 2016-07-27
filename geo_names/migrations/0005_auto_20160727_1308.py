# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_names', '0004_cityalternate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='geoname_id',
        ),
        migrations.RemoveField(
            model_name='countryalternate',
            name='geoname_id',
        ),
    ]
