#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from .data import iso_639_3_codes, iso_639_2_codes


class Language(object):
    def __init__(self, iso):
        self.iso = iso

        try:
            self.name = iso_639_3_codes[iso]
        except KeyError:
            try:
                self.name = iso_639_2_codes[iso]
            except KeyError:
                raise KeyError("Language with iso code '%s' unknown" % iso)

    def __repr__(self):
        return u"Language(iso={})".format(self.iso)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.iso == other.iso and self.name == other.name
