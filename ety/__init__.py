import argparse
from random import choice
from uuid import uuid4

from treelib import Tree

from . import data


def cli():
    parser = argparse.ArgumentParser()
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
            lines.append(prettify_word(origin['word'], origin['lang']['code']))
        print('\n'.join(lines))

    return 0


class Word(object):
    def __init__(self, word, language):
        self.word = word
        self.lang_code = language
        self.lang_name = lang_name(language)
        self.pretty = prettify_word(word, language)


def prettify_word(word, language):
    if language:
        return "%s (%s)" % (word, lang_name(language))
    return word


def lang_name(code):
    for lang in data.langs:
        if lang['iso6393'] == code:
            return lang['name']
    return "Unknown language"


def origins(word, word_lang='eng', recursive=False):
    result = []
    for origin in _origins(word, word_lang, recursive):
        result.append({
            'word': origin.word,
            'lang': {
                'code': origin.lang_code,
                'name': origin.lang_name
            }
        })
    return result


def _origins(word, word_lang='eng', recursive=False):
    row = list(filter(
        lambda entry: entry['a_word'] == word and entry[
            'a_lang'] == word_lang, data.etyms))
    result = []
    for item in row:
        result.append(Word(item['b_word'], item['b_lang']))
    if recursive:
        for origin in result:
            for child in _origins(origin.word, origin.lang_code):
                if origin.word != child.word:
                    result.append(child)
    return result


def _tree(tree_obj, word, parent, parent_word):
    word_origins = _origins(word.word, word_lang=word.lang_code)
    for origin in word_origins:
        key = uuid4()
        # Recursive call to add child origins
        if parent_word == origin.word:
            continue
        tree_obj.create_node(origin.pretty, key, parent=parent)
        _tree(tree_obj, origin, key, origin.word)


def tree(word, word_lang='eng'):
    ety_tree = Tree()

    word_obj = Word(word, word_lang)
    root = word_obj.pretty
    root_key = uuid4()

    # Create parent node
    ety_tree.create_node(root, root_key)

    # Add child etymologies
    _tree(ety_tree, Word(word, word_lang), root_key, word)

    return str(ety_tree)


def random_word(lang='eng'):
    row = list(filter(lambda entry: entry['a_lang'] == lang, data.etyms))
    word = choice(row)['a_word']
    return word
