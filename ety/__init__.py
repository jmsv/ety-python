#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
from random import choice

import colorful

from . import data
from .tree import EtyTree
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

    output = ''
    for word in args.words:
        roots = origins(word, recursive=args.recursive)

        if not roots:
            print("No origins found for word: {}".format(word))
            continue

        if args.tree:
            output += '%s\n\n' % str(tree(word))
        else:
            output += '\n\n%s\n \u2022 ' % colorful.bold(word)
            output += '\n \u2022 '.join(root.pretty for root in roots)

    print(output.strip())

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
    return EtyTree(source_word)


def random_word(lang='eng'):
    row = list(filter(lambda entry: entry['a_lang'] == lang, data.etyms))
    word = choice(row)['a_word']
    return Word(word, lang)
