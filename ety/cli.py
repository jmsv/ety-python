#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import argparse

import ety


def cli():
    parser = argparse.ArgumentParser(prog="ety")
    parser.add_argument("words", type=str, nargs='+',
                        help="the search word(s)")
    parser.add_argument("-r", "--recursive", help="search origins recursively",
                        action="store_true")
    parser.add_argument("-t", "--tree", help="display etymology tree",
                        action="store_true")
    args = parser.parse_args()

    output = ''
    for word in args.words:
        source_word = ety.Word(word, is_source=True)
        roots = ety.origins(word, recursive=args.recursive)

        if not roots:
            print("No origins found for word: {}".format(word))
            continue

        if args.tree:
            output += '%s\n\n' % str(ety.tree(source_word))
        else:
            output += '\n\n%s\n \u2022 ' % source_word
            output += '\n \u2022 '.join(root.pretty for root in roots)

    print(output.strip())

    return 0
