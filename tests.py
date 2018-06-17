#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import ety


def test_circular_etymology():
    """Test to avoid https://github.com/jmsv/ety-python/issues/20
    This method is run with a 10 second timeout (see Makefile test)"""
    ety.origins('software', recursive=True)


def stdout_capture(func):
    """Decorator to capture stdout during a test for testing the command line
    If you need to actually print to stdout during a test, use ._print
    """
    sys_stdout_write = sys.stdout.write

    class MockWriter(object):
        _print = sys_stdout_write

        def __init__(self):
            self._value = u""

        def __call__(self, message):
            self._value += message

        @property
        def value(self):
            # Remove trailing new line so tests make more sense
            return self._value.strip()

        @property
        def lines(self):
            return len(self.value.split("\n"))

    def wrapper(obj):
        output = MockWriter()
        # Override stdout.write with the mock
        sys.stdout.write = output

        # Pass the mock to the test
        result = func(obj, output)

        # Restore stdout
        sys.stdout.write = sys_stdout_write
        return result
    return wrapper


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
