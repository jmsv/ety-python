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
        self._origins = {
            'direct': [],
            'recursive': []
        }
        self._id = u"{}:{}".format(
            self.word.lower(), self.language.iso.lower())

    def origins(self, recursive=False):
        if self.word not in etymwn_data[self.language.iso]:
            # There are no roots for this word
            return []

        roots = [Word(word, lang) for root in
                 etymwn_data[self.language.iso][self.word] for word, lang in
                 root.items()]

        tracked = roots[:]

        if recursive:
            for root in tracked:
                for child in root.origins():
                    # Check word isn't already in tree before appending
                    if child not in tracked and child != self:
                        tracked.append(child)

        self._origins = tracked
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
        return u'Word({word}, {lang} [{iso}])'.format(
            word=self.word, lang=self.language, iso=self.language.iso
        )
