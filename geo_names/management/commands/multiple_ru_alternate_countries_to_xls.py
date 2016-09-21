# coding=utf-8
import xlwt
from django.conf import settings
from django.core.management import BaseCommand, CommandError
from django.db.models import Case, When, Sum, IntegerField, Q

from geo_names.models import Country


class Command(BaseCommand):
    """
    Command for dumping countries data to xls file, which have several alternate names on russian.
    """
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write('Start parsing')

            alternate_countries_list = Country.objects.annotate(
                alt_countries_count=Sum(Case(
                    When(countryalternate__iso_language='ru', then=1),
                    default=0,
                    output_field=IntegerField(),
                )),
            ).filter(Q(alt_countries_count__gt=1) | Q(alt_countries_count=0))

            workbook = xlwt.Workbook(encoding='utf-8')

            sheet = workbook.add_sheet(u'Страны')
            titles = [
                u'ID',
                u'Страна',
                u'Русские варианты перевода',
                u'Yandex вариант перевода',
            ]

            # set titles row
            for index, col in enumerate(titles):
                sheet.write(
                    0,
                    index,
                    col,
                    xlwt.easyxf('font: bold 1; pattern: pattern solid, fore_colour gray25;'),
                )
                if index in [1, 3]:
                    sheet.col(index).width = 7000
                elif index == 2:
                    sheet.col(index).width = 20000
                else:
                    sheet.col(index).width = 2500
            sheet.set_panes_frozen(True)
            sheet.set_horz_split_pos(1)
            sheet.set_vert_split_pos(3)

            # write cities data
            for row, value in enumerate(alternate_countries_list):
                data_list = [
                    value.id,
                    value.name,
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

            workbook.save('tmp/alternate_countries_ru_list.xls')

            self.stdout.write('Successful parsing!')
        else:
            raise CommandError('ERROR: Please set debug mode')
