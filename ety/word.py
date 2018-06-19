#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import colorful

from .data import etyms as etymwn_data
from .language import Language
from .tree import EtyTree

from six import string_types


class Word(object):
    def __init__(self, word, language='eng', is_source=False):
        if not isinstance(word, string_types):
            raise ValueError('word must be a string')
        self.word = word
        self.language = Language(language)
        self.is_source = is_source
        self._origins = None
        self._id = u"{}:{}".format(self.word, self.language.iso)

    def origins(self, recursive=False):
        if self._origins:
            return self._origins

        row = list(filter(
            lambda entry: entry['a_word'] == self.word and entry[
                'a_lang'] == self.language.iso, etymwn_data))

        result = [Word(item['b_word'], item['b_lang']) for item in row]

        if recursive:
            for origin in result:
                for child in origin.origins():
                    # Check word isn't already in tree before appending
                    if child not in result and child != self:
                        result.append(child)

        self._origins = result
        return self._origins

    def tree(self):
        return EtyTree(self)

    @property
    def pretty(self):
        word = colorful.bold(self.word) if self.is_source else self.word
        return u"{word} ({lang})".format(
            word=word,
            lang=self.language.name)

    def __lt__(self, other):
        if isinstance(other, Word):
            return self.pretty < other.pretty
        return self.pretty < other

    def __eq__(self, other):
        if isinstance(other, Word):
            return self._id == other._id
        return self.pretty == other

    def __str__(self):
        return self.pretty

    def __repr__(self):
        return u'Word({word}, language={lang})'.format(
            word=self.word, lang=self.language
        )
