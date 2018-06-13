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

    for word in args.words:
        roots = origins(word, recursive=args.recursive)

        if not roots:
            print("No origins found for word: {}".format(word))
            continue

        if args.tree:
            result = str(tree(word)).strip()
        else:
            result = '\n'
            if word is args.words[0]:
                result = ''
            result += '\033[1m' + word + '\033[0m \n \u2022 '
            result += '\n \u2022 '.join(root.pretty for root in roots)

        print(result)

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
