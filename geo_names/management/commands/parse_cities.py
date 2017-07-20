# coding=utf-8
from __future__ import unicode_literals, print_function

from django.conf import settings
from django.core.management import BaseCommand, CommandError

from geo_names.city_parser import CityParser


class Command(BaseCommand):
    """
    Command for parsing cities file from http://geonames.org/.
    """
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            city_parser = CityParser()
            city_parser.get_cities()
            city_parser.get_alternate_names()

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
