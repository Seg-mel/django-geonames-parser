# coding=utf-8
from __future__ import unicode_literals, print_function

from django.conf import settings
from django.core.management import BaseCommand, CommandError

from geo_names.countries import get_alternate_country_locale_names


class Command(BaseCommand):
    """
    Command for parsing locale names for countries.
    """
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            get_alternate_country_locale_names('ru')

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
