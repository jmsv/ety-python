import sys
from random import choice

from . import data
data.load()


def cli():
    if len(sys.argv) <= 1:
        print("No word supplied\n")
        print("Usage:\n  $ ety <word>\n")
        print("Example:\n  $ ety potato\n  Spanish, Taino")
        return

    # word = sys.argv[1]
    print('Not yet implemented')


def origins(word, word_lang='eng'):
    row = list(filter(lambda entry: entry['a_word'] == word and entry['a_lang'] == word_lang, data.etyms))
    result = []
    for item in row:
        result.append({
            'word': item['b_word'],
            'lang': item['b_lang'],
        })
    return result


def random_word(lang='eng'):
    row = list(filter(lambda entry: entry['a_lang'] == lang, data.etyms))
    word = choice(row)['a_word']
    return word
