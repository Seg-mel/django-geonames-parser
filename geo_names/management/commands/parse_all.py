# coding=utf-8
from __future__ import unicode_literals, print_function

from django.conf import settings
from django.core.management import BaseCommand, CommandError

from geo_names.city_parser import CityParser
from geo_names.country_parser import CountryParser


class Command(BaseCommand):
    """
    Command for parsing countries and cities files from http://geonames.org/.
    """
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            country_parser = CountryParser()
            country_parser.get_countries()
            country_parser.get_alternate_names()
            country_parser.get_alternate_locale_names('ru')

            city_parser = CityParser()
            city_parser.get_cities()
            city_parser.get_alternate_names()
            city_parser.get_alternate_locale_names('ru')

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
