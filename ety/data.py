# encoding: utf-8

import io
import json

from pkg_resources import resource_filename

etyms = []
langs = []


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
    global etyms
    etyms = []
    with io.open(resource_filename(
            'ety', 'wn/etymwn-relety.json'), 'r') as f:
        etyms = json.load(f)


def load_country_codes():
    global langs
    langs = []
    with io.open(resource_filename('ety', 'wn/iso-639-3.json'), 'r') as f:
        countries_json = json.load(f)
    for country in countries_json:
        langs.append({
            'name': country['name'],
            'iso6393': country['iso6393'],
        })


def load():
    load_relety()
    load_country_codes()
