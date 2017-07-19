# coding=utf-8
from __future__ import unicode_literals, print_function

import xlwt
from django.conf import settings
from django.core.management import BaseCommand, CommandError
from django.db.models import Case, When, Sum, IntegerField

from geo_names.models import City


class Command(BaseCommand):
    """
    Command for dumping cities data to xls file, which have several alternate names on russian.
    """
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            alternate_cities_list = City.objects.annotate(
                alt_cities_count=Sum(Case(
                    When(cityalternate__iso_language='ru', then=1),
                    default=0,
                    output_field=IntegerField(),
                )),
            ).filter(alt_cities_count__gt=1).order_by('country__name', 'alt_cities_count')

            workbook = xlwt.Workbook(encoding='utf-8')

            sheet = workbook.add_sheet('Города')
            titles = [
                'ID',
                'Страна',
                'Английское название города',
                'Строка для поиска',
                'Русские варианты перевода',
                'Yandex вариант перевода',
            ]

            # set titles row
            for index, col in enumerate(titles):
                sheet.write(
                    0,
                    index,
                    col,
                    xlwt.easyxf('font: bold 1; pattern: pattern solid, fore_colour gray25;'),
                )
                if index in [1, 2, 3, 5]:
                    sheet.col(index).width = 7000
                elif index == 4:
                    sheet.col(index).width = 20000
                else:
                    sheet.col(index).width = 2500
            sheet.set_panes_frozen(True)
            sheet.set_horz_split_pos(1)
            sheet.set_vert_split_pos(5)

            # write cities data
            for row, value in enumerate(alternate_cities_list):
                data_list = [
                    value.id,
                    '{} ({})'.format(
                        value.country.alternate_names.filter(iso_language='ru').first().name,
                        value.country.name,
                    ),
                    value.name,
                    '{}, {}'.format(value.country.name, value.name),
                    ', '.join([ac.name for ac in value.alternate_names.filter(iso_language='ru')]),
                ]
                for col, col_value in enumerate(data_list):
                    sheet.write(
                        row + 1,
                        col,
                        col_value,
                        xlwt.easyxf(
                            'align: wrap 1; align: vertical top; '
                            'borders: left thin, right thin, top thin, bottom thin;'
                            'pattern: pattern solid, fore_colour light_green;'
                        ),
                    )

            workbook.save('tmp/alternate_cities_ru_list.xls')

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
