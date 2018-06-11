import argparse
from random import choice

from . import data
from .word import Word, Language  # noqa: F401


def cli():
    parser = argparse.ArgumentParser(prog="ety")
    parser.add_argument("words", type=str, nargs='+',
                        help="the search word(s)")
    parser.add_argument("-r", "--recursive", help="search origins recursively",
                        action="store_true")
    parser.add_argument("-t", "--tree", help="display etymology tree",
                        action="store_true")
    args = parser.parse_args()

    if args.tree:
        for word in args.words:
            word_origins = origins(word, recursive=args.recursive)
            if not word_origins:
                print("No origins found for word: '%s'" % word)
                continue
            print(tree(word))
        return 0

    for word in args.words:
        word_origins = origins(word, recursive=args.recursive)
        if not word_origins:
            print("No origins found for word: '%s'" % word)

        lines = []
        for origin in word_origins:
            lines.append(str(origin))
        print('\n'.join(lines))

    return 0


def _get_source_word(word, word_lang):
    if isinstance(word, Word):
        return word
    return Word(word, word_lang)


def origins(word, word_lang='eng', recursive=False):
    source_word = _get_source_word(word, word_lang)
    return source_word.origins(recursive)


def tree(word, word_lang='eng'):
    source_word = _get_source_word(word, word_lang)
    return source_word.tree()


def random_word(lang='eng'):
    row = list(filter(lambda entry: entry['a_lang'] == lang, data.etyms))
    word = choice(row)['a_word']
    return Word(word, lang)
