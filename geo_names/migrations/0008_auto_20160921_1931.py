# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_names', '0007_countrylocalename'),
    ]

    operations = [
        migrations.AddField(
            model_name='citylocalename',
            name='manual_translation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='countrylocalename',
            name='manual_translation',
            field=models.BooleanField(default=False),
        ),
    ]
