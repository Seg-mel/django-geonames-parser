# coding=utf-8
from django.conf import settings
from django.core.management import BaseCommand, CommandError

from geo_names.countries import get_counties, get_alternate_country_names


class Command(BaseCommand):
    """
    Command for parsing countries files from http://geonames.org/.
    """
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            get_counties()
            get_alternate_country_names()

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
