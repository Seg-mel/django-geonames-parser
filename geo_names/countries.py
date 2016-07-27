# coding=utf-8
import csv
import logging
import os

from django.conf import settings

from geo_names.models import Country, CountryAlternate


logger = logging.getLogger(__name__)


COUNTRIES_FILE_PATH = getattr(
    settings,
    'COUNTRIES_FILE_PATH',
    os.path.join(settings.BASE_DIR, 'tmp', 'countryInfo.txt'),
)

ALTERNATE_NAMES_FILE_PATH = getattr(
    settings,
    'ALTERNATE_NAMES_FILE_PATH',
    os.path.join(settings.BASE_DIR, 'tmp', 'alternateNames.txt'),
)

COUNTRY_FIELDS = {
    'geoname_id': 16,
    'name': 4,
    'capital': 5,
    'iso': 0,
    'iso3': 1,
    'iso_numeric': 2,
    'fips': 3,
}

ALTERNATE_COUNTRY_FIELDS = {
    'name': 3,
    'iso_language': 2,
    'geoname_id': 1,
}


def __write_country_to_db(line):
    Country.objects.create(
        id=line[COUNTRY_FIELDS['geoname_id']],
        name=line[COUNTRY_FIELDS['name']].strip(),
        capital=line[COUNTRY_FIELDS['capital']].strip(),
        iso=line[COUNTRY_FIELDS['iso']].strip(),
        iso3=line[COUNTRY_FIELDS['iso3']].strip(),
        iso_numeric=line[COUNTRY_FIELDS['iso_numeric']].strip(),
        fips=line[COUNTRY_FIELDS['fips']].strip(),
    )


def __write_aternate_country_name_to_db(line, country_geoname_id_list):
    if line and not line[0].startswith('#'):
        iso_language = line[ALTERNATE_COUNTRY_FIELDS['iso_language']]
        geoname_id = int(line[ALTERNATE_COUNTRY_FIELDS['geoname_id']])
        if geoname_id in country_geoname_id_list and len(iso_language) in [2, 3]:
            CountryAlternate.objects.create(
                country_id=geoname_id,
                name=line[ALTERNATE_COUNTRY_FIELDS['name']].strip(),
                iso_language=iso_language,
            )


def get_counties():
    try:
        with open(COUNTRIES_FILE_PATH) as country_file:
            for line in csv.reader(country_file, dialect='excel-tab'):
                if line and not line[0].startswith('#'):
                    __write_country_to_db(line)
    except Exception, error:
        logger.debug(error)


def get_alternate_country_names():
    country_geoname_id_list = [v[0] for v in Country.objects.all().values_list('id')]
    try:
        with open(ALTERNATE_NAMES_FILE_PATH) as country_file:
            for line in csv.reader(country_file, dialect='excel-tab'):
                __write_aternate_country_name_to_db(line, country_geoname_id_list)
    except Exception, error:
        logger.debug(error)
