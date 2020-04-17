# -*- coding: utf-8 -*-

from codecs import open as fopen
from os.path import dirname, abspath, join
from setuptools import setup


DIR = dirname(abspath(__file__))
VERSION = '0.3'

with fopen(join(DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'gender_neutral_name',
    version = VERSION,
    description = 'Faker provider for gender neutral name generator',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    keywords = 'faker faker-library faker-provider faker-generator gender-neutral name-generator',
    author = 'Padamja',
    author_email = 'padamja.gupta@gmail.com',
    license='MIT',
    url = 'https://github.com/Padamja/gender_neutral_name',
    download_url = 'https://github.com/Padamja/gender_neutral_name/archive/v{0}.tar.gz'.format(VERSION),
    zip_safe = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2 :: Only',
    ],
    packages = ['gender_neutral_name'],
    install_requires = [
        'Faker'
    ],
)
