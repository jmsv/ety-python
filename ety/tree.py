
import treelib
import ety


class EtyTree(treelib.Tree):

    def __init__(self, word=''):
        if isinstance(word, ("".__class__, u"".__class__)):
            word = ety.Word(word)
        self.source_word = word

        super(EtyTree, self).__init__()

        if not self.source_word.origins():
            return

        self.create_node(word.pretty, word._id, data=word)

        self.add_children(self.source_word)

    def add_children(self, parent):
        for origin in parent.origins():
            key = origin._id

            try:
                self.create_node(
                    origin.pretty, key, parent=parent._id, data=origin
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
