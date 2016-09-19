# coding=utf-8
from django.conf import settings
from django.core.management import BaseCommand, CommandError

from geo_names.cities import get_alternate_city_locale_names


class Command(BaseCommand):
    """
    Command for parsing locale names for cities.
    """
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            get_alternate_city_locale_names('ru')

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
