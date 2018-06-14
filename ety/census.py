import re

from .word import Word

string_types = ("".__class__, u"".__class__)


class Census(object):
    def __init__(self, words, lang='eng'):
        if isinstance(words, ("".__class__, u"".__class__)):
            words = re.split('\s+', words)
        elif isinstance(words, (list, tuple)):
            words = list(words)
        else:
            raise ValueError('words argument must be either string or list')

        assert type(words) is list

        self.words = []
        for word in list(words):
            if isinstance(word, string_types):
                self.words.append(Word(word, lang))
            elif isinstance(word, Word):
                self.words.append(word)
            else:
                raise ValueError("Invalid word type: '%s'.\ Words must\
                    be ety.Word objects or strings" % str(type(word)))

    def __eq__(self, other):
        return self.words == other.words
