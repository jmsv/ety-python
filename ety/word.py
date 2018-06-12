import treelib

from .data import etyms as etymwn_data
from .language import Language


class Word(object):
    def __init__(self, word, language='eng'):
        if not isinstance(word, ("".__class__, u"".__class__)):
            raise ValueError('word must be a string')
        self.word = word
        self.language = Language(language)
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
                    no_duplicates = child not in result and child != self

                    if origin.word != child.word and no_duplicates:
                        result.append(child)

        self._origins = result
        return self._origins

    def tree(self):
        ety_tree = treelib.Tree()

        word_obj = Word(self.word, self.language.iso)
        root = word_obj.pretty
        root_key = self._id

        # Create parent node
        ety_tree.create_node(root, root_key, data=self)

        # Add child etymologies
        self._tree(ety_tree, root_key)

        return ety_tree

    def _tree(self, tree_obj, parent):
        source_word = Word(self.word, self.language.iso)
        word_origins = source_word.origins()

        for origin in word_origins:
            key = origin._id
            # Recursive call to add child origins
            if self.word == origin.word:
                continue

            try:
                tree_obj.create_node(
                    origin.pretty, key, parent=parent, data=origin
                )
            except treelib.exceptions.DuplicatedNodeIdError:
                continue
            origin._tree(tree_obj, key)

    @property
    def pretty(self):
        return u"{word} ({lang})".format(
            word=self.word,
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
