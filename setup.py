#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'django-jquery-ui',
    version = '0.2',
    description = "jquery-ui django app - bundles jQuery UI for django-staticfiles",
    long_description = open('README.rst').read(),
    author = 'Aljosa Mohorovic',
    author_email = 'aljosa.mohorovic@gmail.com',
    url='http://github.com/aljosa/django-jquery-ui/',
    packages = find_packages(),
    include_package_data = True,
    license = "MIT License",
    keywords = "django jquery ui staticfiles",
    platforms = ['any'],
)
