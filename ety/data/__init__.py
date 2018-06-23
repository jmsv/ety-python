#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import io
import json

from pkg_resources import resource_filename


def load_etymologies():
    resource = resource_filename('ety', 'data/etymologies.json')
    with io.open(resource, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_country_codes():
    resource = resource_filename('ety', 'data/iso-639-3.json')
    with io.open(resource, 'r', encoding='utf-8') as f:
        return json.load(f)


etyms = load_etymologies()
langs = load_country_codes()
