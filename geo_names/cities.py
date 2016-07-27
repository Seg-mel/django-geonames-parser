# coding=utf-8
import csv
import logging
import os
import sys

from django.conf import settings

from geo_names.models import City, Country, CityAlternate


csv.field_size_limit(sys.maxsize)

logger = logging.getLogger(__name__)


ALL_COUNTRIES_FILE_PATH = getattr(
    settings,
    'ALL_COUNTRIES_FILE_PATH',
    os.path.join(settings.BASE_DIR, 'tmp', 'allCountries.txt'),
)

ALTERNATE_NAMES_FILE_PATH = getattr(
    settings,
    'ALTERNATE_NAMES_FILE_PATH',
    os.path.join(settings.BASE_DIR, 'tmp', 'alternateNames.txt'),
)

CITY_FEATURE_CLASS = getattr(settings, 'CITY_FEATURE_CLASS', 'P')

CITY_FEATURE_CODES = getattr(settings, 'CITY_FEATURE_CODES', None)

CITY_FIELDS = {
    'counrty': 8,
    'name': 1,
    'latitude': 4,
    'longitude': 5,
    'timezone': 17,
    'geoname_id': 0,
    'feature_class': 6,
    'feature_code': 7,
    'date_modification': 18,
}

ALTERNATE_CITY_FIELDS = {
    'name': 3,
    'iso_language': 2,
    'geoname_id': 1,

}


def get_cities():
    for_index = 0
    debug_line = None
    city_list = []
    country_id_dict = dict(Country.objects.values_list('iso', 'geoname_id'))
    try:
        with open(ALL_COUNTRIES_FILE_PATH) as country_file:
            for line in csv.reader(country_file, dialect='excel-tab'):
                if line and not line[CITY_FIELDS['geoname_id']].startswith('#'):
                    parse_condition = line[CITY_FIELDS['feature_class']] == CITY_FEATURE_CLASS
                    if CITY_FEATURE_CODES:
                        parse_condition = parse_condition and line[CITY_FIELDS['feature_code']] in CITY_FEATURE_CODES

                    if parse_condition:
                        debug_line = line
                        city_list.append(City(
                            id=line[CITY_FIELDS['geoname_id']],
                            country_id=country_id_dict[line[CITY_FIELDS['counrty']]],
                            name=line[CITY_FIELDS['name']],
                            latitude=line[CITY_FIELDS['latitude']],
                            longitude=line[CITY_FIELDS['longitude']],
                            timezone=line[CITY_FIELDS['timezone']],
                            feature_class=line[CITY_FIELDS['feature_class']],
                            feature_code=line[CITY_FIELDS['feature_code']],
                            date_modification=line[CITY_FIELDS['date_modification']],
                        ))
                    if divmod(for_index, 500000)[1] == 0:
                        logger.info(for_index)
                        City.objects.bulk_create(city_list)
                        city_list = []
                    for_index += 1
            City.objects.bulk_create(city_list)
    except Exception, error:
        logger.debug(u'{}\n{}'.format(error, unicode(debug_line)))


def get_alternate_city_names():
    for_index = 0
    debug_line = None
    city_geoname_id_set = set([v[0] for v in City.objects.all().values_list('id')])
    alternate_city_list = []
    try:
        with open(ALTERNATE_NAMES_FILE_PATH) as country_file:
            for line in csv.reader(country_file, dialect='excel-tab'):
                debug_line = line
                if line and not line[0].startswith('#'):
                    iso_language = line[ALTERNATE_CITY_FIELDS['iso_language']]
                    geoname_id = int(line[ALTERNATE_CITY_FIELDS['geoname_id']])
                    if geoname_id in city_geoname_id_set and len(iso_language) in [2, 3]:
                        alternate_city_list.append(CityAlternate(
                            city_id=geoname_id,
                            name=line[ALTERNATE_CITY_FIELDS['name']],
                            iso_language=iso_language,
                        ))
                    if divmod(for_index, 500000)[1] == 0:
                        logger.info(for_index)
                        CityAlternate.objects.bulk_create(alternate_city_list)
                        alternate_city_list = []
                    for_index += 1
            CityAlternate.objects.bulk_create(alternate_city_list)
    except Exception, error:
        logger.debug(u'{}\n{}'.format(error, unicode(debug_line)))
