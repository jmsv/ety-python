# encoding: utf-8

import io
import json

from pkg_resources import resource_filename


def parse_row(data_row):
    a_lang, a_word = data_row[0].split(': ')
    b_lang, b_word = data_row[2].split(': ')
    return {
        'a_lang': a_lang,
        'a_word': a_word,
        'b_lang': b_lang,
        'b_word': b_word,
    }


def load_relety():
    resource = resource_filename('ety', 'wn/etymwn-relety.json')
    with io.open(resource, 'r', encoding='utf-8') as f:
        etyms = json.load(f)
    return etyms


def load_country_codes():
    langs = []
    resource = resource_filename('ety', 'wn/iso-639-3.json')
    with io.open(resource, 'r', encoding='utf-8') as f:
        countries_json = json.load(f)
    for country in countries_json:
        langs.append({
            'name': country['name'],
            'iso6393': country['iso6393'],
        })
    return langs


etyms = load_relety()
langs = load_country_codes()
