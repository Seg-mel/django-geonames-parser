# coding=utf-8
from __future__ import unicode_literals, print_function

from django.db import models
from django.db.models import CASCADE

from .country import Country


class CountryLocaleName(models.Model):
    country = models.ForeignKey(Country, on_delete=CASCADE)

    name = models.CharField(max_length=255)
    iso_language = models.CharField(max_length=3)

    manual_translation = models.BooleanField(default=False)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
