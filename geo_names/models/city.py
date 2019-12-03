# coding=utf-8
from __future__ import unicode_literals, print_function

from django.db import models
from django.db.models import CASCADE
from django.utils.translation import get_language

from .country import Country


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=CASCADE)

    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    timezone = models.CharField(max_length=255)
    feature_class = models.CharField(max_length=1)
    feature_code = models.CharField(max_length=10)
    date_modification = models.CharField(max_length=255)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    @property
    def alternate_names(self):
        return self.cityalternate_set.all()

    @property
    def locale_names(self):
        return self.citylocalename_set.all()

    @property
    def name_i18n(self):
        language = get_language()

        if language == 'ru':
            locale_name_object = self.locale_names.filter(iso_language='ru').first()

            if locale_name_object:
                return locale_name_object.name

        return self.name
