# django-geonames-parser
Cities and countries parser based on data from [GeoNames](http://www.geonames.org/). 
Also supports parsing alternate names and local names for cities and countries.
Tested on Python 2.7/3.6 and Django 1.8/1.11.

## Installation
`pip install git+https://github.com/Seg-mel/django-geonames-parser.git`

## Settings
Add app to INSTALLED_APPS
```python
INSTALLED_APPS = [
    ...
    'geo_names',
    ...
]
```

Set path to countries dump file `COUNTRIES_FILE_PATH`. [Download this file](http://download.geonames.org/export/dump/countryInfo.txt).
```python
COUNTRIES_FILE_PATH = '<your_directory_with_dumps>/countryInfo.txt'
```

Set path to alternate names dump file `ALTERNATE_NAMES_FILE_PATH`. [Download this file](http://download.geonames.org/export/dump/alternateNames.zip).
```python
ALTERNATE_NAMES_FILE_PATH = '<your_directory_with_dumps>/alternateNames.txt'
```

Set path to alternate names dump file `ALL_COUNTRIES_FILE_PATH`. You can download one file from list:
* [allCountries.zip](http://download.geonames.org/export/dump/allCountries.zip) - all countries combined in one file, see 'geoname' table for columns
* [cities1000.zip](http://download.geonames.org/export/dump/cities1000.zip) - all cities with a population > 1000 or seats of adm div (ca 150.000), see 'geoname' table for columns
* [cities5000.zip](http://download.geonames.org/export/dump/cities5000.zip) - all cities with a population > 5000 or PPLA (ca 50.000), see 'geoname' table for columns
* [cities15000.zip](http://download.geonames.org/export/dump/cities15000.zip) - all cities with a population > 15000 or capitals (ca 25.000), see 'geoname' table for columns
```python
ALL_COUNTRIES_FILE_PATH = '<your_directory_with_dumps>/cities15000.txt'
```

Set value for feature class `CITY_FEATURE_CLASS`. Default value is 'P'.
* A: country, state, region,...
* H: stream, lake, ...
* L: parks,area, ...
* P: city, village,...
* R: road, railroad 
* S: spot, building, farm
* T: mountain,hill,rock,... 
* U: undersea
* V: forest,heath,...
```python
CITY_FEATURE_CLASS = 'P'
```

Set value for feature codes `CITY_FEATURE_CODES`. Default value is 'None', with this value cities with all codes are parsed. A list of all codes is available [here](http://www.geonames.org/export/codes.html).
```python
CITY_FEATURE_CODES = ['PPL', 'PPLA', 'PPLF']
```

Data dumps and documentation are available [here](http://download.geonames.org/export/dump/).

## Management commands
**parse_all** - parse cities, countries, alternate names, names for locale 'ru' <br />
**parse_cities** - parse cities with alternate names <br />
**parse_city_locale_names** - parse names for 'ru' locale for cities that were parsed earlier and are already in database <br />
**parse_countries** - parse countries with alternate names <br />
**parse_country_locale_names** - parse names for 'ru' locale for countries that were parsed earlier and are already in database <br />


## GeoNames license
This work is licensed under a [Creative Commons Attribution 3.0 License](https://creativecommons.org/licenses/by/3.0/)
