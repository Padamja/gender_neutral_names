#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from codecs import open as fopen
from os.path import dirname, abspath, join
from setuptools import setup, find_packages


DIR = dirname(abspath(__file__))

with fopen(join(DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'gender_neutral_name',
    version = ,
    description = 'Faker provider for gender neutral name generator',
    long_description = long_description,
    keywords = 'faker faker-library faker-provider faker-generator gender-neutral name-generator',
    author = 'Padamja Gupta',
    author_email = 'padamja.gupta@gmail.com',
    url = '',
    download_url = '/archive/v{0}.zip'.format(VERSION),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2 :: Only',
    ],
    packages = find_packages(exclude=['data', 'src']),
    install_requires = [
        'Faker', 'json'
    ],
)
