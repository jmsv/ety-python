#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
import ety


def test_circular_etymology():
    """Test to avoid https://github.com/jmsv/ety-python/issues/20
    This method is run with a 10 second timeout (see Makefile test)"""
    ety.origins('software', recursive=True)


class TestEty(unittest.TestCase):

    def test_origins(self):
        o = ety.origins(ety.random_word())
        self.assertGreater(len(o), 0)

    def test_origins_recursion(self):
        o = ety.origins(ety.random_word(), recursive=True)
        self.assertGreater(len(o), 0)
        o = ety.origins('iland', recursive=True)
        self.assertGreater(len(o), 0)

    def test_lang(self):
        self.assertEqual(ety.Language('eng').name, 'English')
        self.assertEqual(ety.Language('lat').name, 'Latin')
        self.assertEqual(ety.Language('enm').name,
                         'Middle English (1100-1500)')

    def test_tree(self):
        self.assertGreaterEqual(len(str(
            ety.tree('aerodynamically')).split('\n')), 10)
        self.assertGreaterEqual(len(str(
            ety.tree('fabric')).split('\n')), 4)


if __name__ == '__main__':
    unittest.main()
