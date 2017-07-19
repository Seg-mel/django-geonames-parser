# coding=utf-8
from __future__ import unicode_literals, print_function

from django.db import models
from django.utils.translation import get_language


class Country(models.Model):
    name = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    iso = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    iso_numeric = models.CharField(max_length=3)
    fips = models.CharField(max_length=3)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    @property
    def alternate_names(self):
        return self.countryalternate_set.all()

    @property
    def locale_names(self):
        return self.countrylocalename_set.all()

    @property
    def name_i18n(self):
        language = get_language()

        if language == 'ru':
            locale_name_object = self.locale_names.filter(iso_language='ru').first()

            if locale_name_object:
                return locale_name_object.name

        return self.name
