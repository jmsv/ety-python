import csv

from pkg_resources import resource_filename

origins_dict = {}
etyms = []


def parse_row(data_row):
    a_lang, a_word = data_row[0].split(': ')
    # rel = data_row[1].replace('rel:', '').strip()
    b_lang, b_word = data_row[2].split(': ')
    return {
        'a_lang': a_lang,
        'a_word': a_word,
        # 'rel': rel,
        'b_lang': b_lang,
        'b_word': b_word,
    }


def load():
    global etyms
    etyms = []
    with open(resource_filename('ety', 'wn/etymwn-relety.tsv'), 'r') as f:
        tsv_in = csv.reader(f, delimiter='\t')
        for row in tsv_in:
            etyms.append(parse_row(row))
