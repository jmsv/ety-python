#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from random import choice

from . import data
from .census import Census
from .cli import cli  # noqa: F401
from .tree import EtyTree
from .word import Word, Language  # noqa: F401


def _get_source_word(word, word_lang, color=False):
    if isinstance(word, Word):
        return word
    return Word(word, word_lang, color=color)


def origins(word, word_lang="eng", recursive=False, color=False):
    source_word = _get_source_word(word, word_lang, color)
    return source_word.origins(recursive)


def tree(word, word_lang="eng", color=False):
    source_word = _get_source_word(word, word_lang, color)
    return EtyTree(source_word)


def random_word(lang="eng"):
    w = choice(list(data.etyms[lang]))
    return Word(w, lang)


def census(words):
    return Census(words)
