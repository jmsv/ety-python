#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import re

from six import string_types

from .word import Word


class Census(object):
    def __init__(self, words, language="eng"):
        self.words = []
        self._origins = {"direct": [], "recursive": []}

        if isinstance(words, string_types):
            words = list(re.split("\s+", words))  # Split words by whitespace
        elif isinstance(words, (list, tuple)):
            words = list(words)
        else:
            raise ValueError("words argument must be either string or list")

        for word in list(words):
            if isinstance(word, string_types):
                self.words.append(Word(word, language))
            elif isinstance(word, Word):
                self.words.append(word)
            else:
                raise ValueError(
                    "Invalid word type: '%s'.\ Words must\
                    be ety.Word objects or strings"
                    % str(type(word))
                )

    def origins(self, recursive=False):
        search = "recursive" if recursive else "direct"

        o = self._origins[search]

        # Return cached direct or recursive origin searches if already searched
        if o:
            return o

        for word in self.words:
            o.extend(word.origins(recursive=recursive))

        return o

    def __eq__(self, other):
        return self.words == other.words
