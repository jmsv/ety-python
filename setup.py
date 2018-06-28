#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ety',
    version='1.1.0',
    description='find the etymological origins of a word',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jmsv/ety-python',
    author='James Vickery',
    author_email='dev@jamesvickery.net',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    keywords='etymology origins english language words',
    packages=['ety', 'ety/data'],
    install_requires=[
        "treelib", "colorful", "six",
    ],
    extras_require={
        'dev': ['flake8'],
    },
    package_data={
        'ety': ['data/etymologies.json', 'data/iso-639-3.json'],
    },
    entry_points={
        'console_scripts': [
            'ety=ety:cli',
        ],
    },
    project_urls={
        'Source': 'https://github.com/jmsv/ety-python',
        'Bug Reports': 'https://github.com/jmsv/ety-python/issues',
    },
)
