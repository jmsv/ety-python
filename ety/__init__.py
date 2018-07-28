#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from random import choice

from . import data
from .census import Census
from .cli import cli  # noqa: F401
from .tree import EtyTree
from .word import Word, Language  # noqa: F401


__version__ = "1.3.1"


def _get_source_word(word, language, color=False):
    if isinstance(word, Word):
        return word
    return Word(word, language, color=color)


def origins(word, language="eng", recursive=False, color=False):
    source_word = _get_source_word(word, language, color)
    return source_word.origins(recursive)


def tree(word, language="eng", color=False):
    source_word = _get_source_word(word, language, color)
    return EtyTree(source_word)


def random_word(language="eng"):
    w = choice(list(data.etyms[language]))
    return Word(w, language)


def census(words):
    return Census(words)
