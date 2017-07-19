# coding=utf-8
from __future__ import unicode_literals, print_function

from django.db import models

from .city import City


class CityAlternate(models.Model):
    city = models.ForeignKey(City)

    name = models.CharField(max_length=255)
    iso_language = models.CharField(max_length=3)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
