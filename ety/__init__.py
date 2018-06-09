import argparse
from random import choice
from uuid import uuid4

from treelib import Tree

from . import data


def cli():
    parser = argparse.ArgumentParser(prog="ety")
    parser.add_argument("words", type=str, nargs='+',
                        help="the search word(s)")
    parser.add_argument("-r", "--recursive", help="search origins recursively",
                        action="store_true")
    parser.add_argument("-t", "--tree", help="display etymology tree",
                        action="store_true")
    args = parser.parse_args()

    if args.tree:
        for word in args.words:
            word_origins = origins(word, recursive=args.recursive)
            if not word_origins:
                print("No origins found for word: '%s'" % word)
                continue
            print(tree(word))
        return 0

    for word in args.words:
        word_origins = origins(word, recursive=args.recursive)
        if not word_origins:
            print("No origins found for word: '%s'" % word)

        lines = []
        for origin in word_origins:
            lines.append(origin.pretty)
        print('\n'.join(lines))

    return 0


class Word(object):
    def __init__(self, word, language='eng'):
        self.word = word
        self.lang_code = language
        self.lang_name = self._find_lang_name(language)
        self._origins = []
        self._tree = Tree()

    @property
    def pretty(self):
        return "{word} ({lang})".format(
            word=self.word,
            lang=self.lang_name)

    @property
    def origins(self):
        if not self._origins:
            row = list(filter(
                lambda entry: (
                    entry['a_word'].lower() == self.word.lower() and
                    entry['a_lang'].lower() == self.lang_code.lower()),
                data.etyms))

            self._origins = [
                Word(item['b_word'], item['b_lang'])
                for item in row if item['b_word'] != self.word]

        return self._origins

    @property
    def tree(self):
        if not self._tree:
            ety_tree = Tree()

            root_key = uuid4()

            # Create parent node
            ety_tree.create_node(self, root_key)

            def _tree(tree_obj, word, parent, parent_word):
                word_origins = origins(word.word, word_lang=word.lang_code)
                for origin in word_origins:
                    key = uuid4()
                    # Recursive call to add child origins
                    if parent_word == origin.word:
                        continue
                    tree_obj.create_node(origin, key, parent=parent)
                    _tree(tree_obj, origin, key, origin.word)
            # Add child etymologies
            _tree(ety_tree, self, root_key, self.word)

            self._tree = ety_tree

        return self._tree

    def _find_lang_name(self, code):
        for lang in data.langs:
            if lang['iso6393'] == code:
                return lang['name']
        return "Unknown language"

    def __lt__(self, other):
        if isinstance(other, Word):
            return self.pretty < other.pretty
        return self.pretty < other

    def __str__(self):
        return self.pretty

    def __repr__(self):
        return 'Word({word}, language={lang})'.format(
            word=self.word, lang=self.lang_code
        )


def origins(word, word_lang='eng', recursive=False):
    source_word = Word(word, word_lang)

    result = []

    for origin in source_word.origins:
        result.append(origin)

        if recursive:
            for child in origins(origin.word, origin.lang_code, True):
                if origin.word != child.word:
                    result.append(child)
    return result


def tree(word, word_lang='eng'):
    source_word = Word(word, word_lang)

    return source_word.tree


def random_word(lang='eng'):
    row = list(filter(lambda entry: entry['a_lang'] == lang, data.etyms))
    word = Word(choice(row)['a_word'], lang)
    return word
