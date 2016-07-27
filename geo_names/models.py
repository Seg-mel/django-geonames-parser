# coding=utf-8
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
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

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)


class City(models.Model):
    country = models.ForeignKey(Country)

    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    timezone = models.CharField(max_length=255)
    feature_class = models.CharField(max_length=1)
    feature_code = models.CharField(max_length=10)
    date_modification = models.CharField(max_length=255)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)


class CityAlternate(models.Model):
    city = models.ForeignKey(City)

    name = models.CharField(max_length=255)
    iso_language = models.CharField(max_length=3)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
