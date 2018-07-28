#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import colorful
from six import string_types

from .data import etyms as etymwn_data
from .language import Language
from .tree import EtyTree


class Word(object):
    def __init__(self, word, language="eng", color=False):
        if not isinstance(word, string_types):
            raise TypeError("word must be a string")
        self._word = word

        if isinstance(language, Language):
            self._language = language
        else:
            self._language = Language(language)

        self.color = bool(color)

        self._origins = {"direct": [], "recursive": []}
        self._id = u"{}:{}".format(self.word, self.language.iso)

    def origins(self, recursive=False):
        search = "recursive" if recursive else "direct"

        if (
            self.language.iso not in etymwn_data
            or self.word not in etymwn_data[self.language.iso]
        ):
            # There are no roots for this word
            return []

        roots = [
            Word(word, lang)
            for root in etymwn_data[self.language.iso][self.word]
            for word, lang in root.items()
        ]

        tracked = roots[:]

        if recursive:
            for root in tracked:
                for child in root.origins():
                    # Check word isn't already in tree before appending
                    if child not in tracked and child != self:
                        tracked.append(child)

        self._origins[search] = tracked
        return self._origins[search]

    def tree(self):
        return EtyTree(self)

    @property
    def word(self):
        return self._word

    @property
    def language(self):
        return self._language

    @property
    def pretty(self):
        word = colorful.bold(self.word) if self.color else self.word
        return u"{word} ({lang})".format(word=word, lang=self.language.name)

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
        return u"Word({word}, {lang} [{iso}])".format(
            word=self.word, lang=self.language, iso=self.language.iso
        )

    def __len__(self):
        return len(self.word)

    @property
    def __dict__(self):
        return {"id": self._id, "word": self.word, "language": self.language.__dict__}
