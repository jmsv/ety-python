#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from random import choice

from . import data
from .census import Census
from .cli import cli  # noqa: F401
from .tree import EtyTree
from .word import Word, Language  # noqa: F401


def _get_source_word(word, word_lang):
    if isinstance(word, Word):
        return word
    return Word(word, word_lang, is_source=True)


def origins(word, word_lang='eng', recursive=False):
    source_word = _get_source_word(word, word_lang)
    return source_word.origins(recursive)


def tree(word, word_lang='eng'):
    source_word = _get_source_word(word, word_lang)
    return EtyTree(source_word)


def random_word(lang='eng'):
    w = choice(list(data.etyms[lang]))
    return Word(w, lang)


def census(words):
    return Census(words)
