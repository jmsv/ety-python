#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import treelib
import ety


class EtyTree(treelib.Tree):
    def __init__(self, word):
        if not isinstance(word, ety.Word):
            raise TypeError("word must be an instance of 'ety.Word'")
        self.source_word = word

        super(EtyTree, self).__init__()

        if not self.source_word.origins():
            return

        self.create_node(word.pretty, word._id, data=word.__dict__)

        self.add_children(self.source_word)

    def add_children(self, parent):
        for origin in parent.origins():
            key = origin._id

            try:
                self.create_node(
                    origin.pretty, key, parent=parent._id, data=origin.__dict__
                )
            except treelib.exceptions.DuplicatedNodeIdError:
                continue

            self.add_children(origin)

    def __bool__(self):
        return bool(self.source_word.origins())

    def __str__(self):
        try:
            return super(EtyTree, self).__str__().strip()
        except treelib.exceptions.NodeIDAbsentError:
            return ""

    def __repr__(self):
        return u"EtyTree(word='{}')".format(self.source_word.word)

    @property
    def __dict__(self):
        return self.to_dict(with_data=True)
