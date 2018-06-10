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
        if not isinstance(word, ("".__class__, u"".__class__)):
            raise ValueError('word must be a string')
        self.word = word
        self.lang_code = language
        self.lang_name = lang_name(language)

    def origins(self, recursive=False):
        result = []
        for origin in self._origins(recursive):
            result.append({
                'word': origin.word,
                'lang': {
                    'code': origin.lang_code,
                    'name': origin.lang_name
                }
            })
        return result

    def _origins(self, recursive=False):
        row = list(filter(
            lambda entry: entry['a_word'] == self.word and entry[
                'a_lang'] == self.lang_code, data.etyms))
        result = []
        for item in row:
            result.append(Word(item['b_word'], item['b_lang']))
        if recursive:
            for origin in result:
                for child in origin._origins():
                    if origin.word != child.word:
                        result.append(child)
        return result

    def tree(self):
        ety_tree = Tree()

        word_obj = Word(self.word, self.lang_code)
        root = word_obj.pretty
        root_key = uuid4()

        # Create parent node
        ety_tree.create_node(root, root_key)

        # Add child etymologies
        self._tree(ety_tree, root_key, self.word)

        return str(ety_tree)

    def _tree(self, tree_obj, parent, parent_word):
        source_word = _get_source_word(self.word, self.lang_code)
        word_origins = source_word._origins()

        for origin in word_origins:
            key = uuid4()
            # Recursive call to add child origins
            if parent_word == origin.word:
                continue
            tree_obj.create_node(origin.pretty, key, parent=parent)
            origin._tree(tree_obj, key, origin.word)

    @property
    def pretty(self):
        return u"{word} ({lang})".format(
            word=self.word,
            lang=self.lang_name)

    def __lt__(self, other):
        if isinstance(other, Word):
            return self.pretty < other.pretty
        return self.pretty < other

    def __str__(self):
        return self.pretty

    def __repr__(self):
        return u'Word({word}, language={lang})'.format(
            word=self.word, lang=self.lang_code
        )


def lang_name(code):
    for lang in data.langs:
        if lang['iso6393'] == code:
            return lang['name']
    return "Unknown language"


def _get_source_word(word, word_lang):
    if isinstance(word, Word):
        return word
    return Word(word, word_lang)


def origins(word, word_lang='eng', recursive=False):
    source_word = _get_source_word(word, word_lang)
    return source_word.origins(recursive)


def tree(word, word_lang='eng'):
    source_word = _get_source_word(word, word_lang)
    return source_word.tree()


def random_word(lang='eng'):
    row = list(filter(lambda entry: entry['a_lang'] == lang, data.etyms))
    word = choice(row)['a_word']
    return Word(word, lang)
