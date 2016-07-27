# coding=utf-8
from django.conf import settings
from django.core.management import BaseCommand, CommandError

from geo_names.cities import get_cities, get_alternate_city_names


class Command(BaseCommand):
    """
    Command for parsing cities file from http://geonames.org/.
    """
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            get_cities()
            get_alternate_city_names()

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
