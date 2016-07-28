# coding=utf-8
from setuptools import find_packages, setup

__author__ = 'Andrey Musikhin'
__version__ = '0.1'

setup(
    name='django-geonames-parser',
    version=__version__,
    description='Django GeoNames parser',
    author=__author__,
    author_email='melomansegfault@gmail.com',
    url='https://github.com/Seg-mel/django-geonames-parser',
    license='MIT',
    packages=find_packages(exclude=('example',)),
    install_requires=[
        'Django>=1.8.4',
    ],
    include_package_data=True,
    keywords=['django', 'geonames', 'parser'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
