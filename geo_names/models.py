# coding=utf-8
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    geoname_id = models.PositiveIntegerField()
    iso = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    iso_numeric = models.CharField(max_length=3)
    fips = models.CharField(max_length=3)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)


class CountryAlternate(models.Model):
    country = models.ForeignKey(Country)

    name = models.CharField(max_length=255)
    iso_language = models.CharField(max_length=3)
    geoname_id = models.PositiveIntegerField()

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

