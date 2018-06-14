#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from .data import langs


class Language(object):
    def __init__(self, iso):
        self.iso = iso
        self.name = None

        try:
            self.name = langs[iso]
        except KeyError:
            raise KeyError('Language with iso code \'%s\' unknown' % iso)

    def __repr__(self):
        return u'Language(iso={})'.format(self.iso)

    def __str__(self):
        return self.name
