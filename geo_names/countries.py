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


def __write_country_to_db(line):
    Country.objects.create(
        name=line[4].strip(),
        capital=line[5].strip(),
        geoname_id=line[16],
        iso=line[0].strip(),
        iso3=line[1].strip(),
        iso_numeric=line[2],
        fips=line[3].strip(),
    )


def __write_aternate_country_name_to_db(line, country_geoname_id_list):
    if line and not line[0].startswith('#'):
        geoname_id = int(line[1])
        iso_language = line[2]
        name = line[3]
        if geoname_id in country_geoname_id_list and len(iso_language) in [2, 3]:
            CountryAlternate.objects.create(
                country=Country.objects.get(geoname_id=int(geoname_id)),
                name=name,
                iso_language=iso_language,
                geoname_id=geoname_id,
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
    country_geoname_id_list = [v[0] for v in Country.objects.all().values_list('geoname_id')]
    try:
        with open(ALTERNATE_NAMES_FILE_PATH) as country_file:
            for line in csv.reader(country_file, dialect='excel-tab'):
                __write_aternate_country_name_to_db(line, country_geoname_id_list)
    except Exception, error:
        logger.debug(error)
