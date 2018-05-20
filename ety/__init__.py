import sys
from random import choice

from . import data

# Load etymology data
data.load()


def cli():
    if len(sys.argv) <= 1:
        print("No word supplied\n")
        print("Usage:\n  $ ety <word>\n")
        print("Example:\n  $ ety potato\n  Spanish, Taino")
        return 1

    word = sys.argv[1]
    o = origins(word, recursive=True)
    print(prettify_origins(o))
    return 0


def prettify_origins(origins_list):
    lines = []
    for origin in origins_list:
        lines.append("%s (%s)" % (origin['word'], lang_name(origin['lang'])))
    return '\n'.join(lines)


def origins(word: str, word_lang='eng', recursive=False) -> list:
    row = list(filter(lambda entry: entry['a_word'] == word and entry['a_lang'] == word_lang, data.etyms))
    result = []
    for item in row:
        result.append({
            'word': item['b_word'],
            'lang': item['b_lang'],
        })
    if recursive:
        for origin in result:
            result.extend(origins(origin['word'], origin['lang']))
    return result


def lang_name(code: str):
    for lang in data.langs:
        if lang['iso6393'] == code:
            return lang['name']


def random_word(lang: str='eng') -> str:
    row = list(filter(lambda entry: entry['a_lang'] == lang, data.etyms))
    word = choice(row)['a_word']
    return word
