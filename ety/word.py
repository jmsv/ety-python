from uuid import uuid4

from treelib import Tree

from .data import etyms as etymwn_data
from .language import Language


class Word(object):
    def __init__(self, word, language='eng'):
        if not isinstance(word, ("".__class__, u"".__class__)):
            raise ValueError('word must be a string')
        self.word = word
        self.language = Language(language)
        self._origins = None

    def origins(self, recursive=False):
        if self._origins:
            return self._origins

        row = list(filter(
            lambda entry: entry['a_word'] == self.word and entry[
                'a_lang'] == self.language.iso, etymwn_data))

        result = []
        for item in row:
            result.append(Word(item['b_word'], item['b_lang']))
        if recursive:
            for origin in result:
                for child in origin.origins():
                    if origin.word != child.word:
                        result.append(child)

        self._origins = result
        return self._origins

    def tree(self):
        ety_tree = Tree()

        word_obj = Word(self.word, self.language.iso)
        root = word_obj.pretty
        root_key = uuid4()

        # Create parent node
        ety_tree.create_node(root, root_key)

        # Add child etymologies
        self._tree(ety_tree, root_key)

        return str(ety_tree).strip()

    def _tree(self, tree_obj, parent):
        source_word = Word(self.word, self.language.iso)
        word_origins = source_word.origins()

        for origin in word_origins:
            key = uuid4()
            # Recursive call to add child origins
            if self.word == origin.word:
                continue

            tree_obj.create_node(origin.pretty, key, parent=parent)
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

    def __str__(self):
        return self.pretty

    def __repr__(self):
        return u'Word({word}, language={lang})'.format(
            word=self.word, lang=self.language
        )
