# coding=utf-8
import xlrd
from django.conf import settings
from django.core.management import BaseCommand, CommandError
from django.utils.timezone import now

from geo_names.models import CountryLocaleName, Country


class Command(BaseCommand):
    """
    Command for parsing countries from xls file with manual translation names.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--file',
            type=str,
            default='',
            help='XLS file'
        )

    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            file_path = options.get('file') or './tmp/ru_countries.xls'

            try:
                xls_file = xlrd.open_workbook(file_path)
            except:
                raise CommandError('ERROR: File not found')

            sheet = xls_file.sheet_by_index(0)

            for row in range(sheet.nrows):
                if row > 0:
                    CountryLocaleName.objects.create(
                        country=Country.objects.get(pk=int(sheet.row(row)[0].value)),
                        name=sheet.row(row)[3].value.strip(),
                        iso_language='ru',
                        manual_translation=True,
                        datetime_create=now(),
                        datetime_update=now(),
                    )

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
