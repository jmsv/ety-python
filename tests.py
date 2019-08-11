#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import ety


def test_circular_etymology():
    """Test to avoid https://github.com/jmsv/ety-python/issues/20
    This method is run with a 10 second timeout (see Makefile test)"""
    ety.origins("software", recursive=True)


def stdout_capture(func):
    """Decorator to capture stdout during a test for testing the command line
    If you need to actually print to stdout during a test, use ._print"""
    sys_stdout = sys.stdout

    class MockWriter(object):
        _print = sys_stdout.write

        def __init__(self):
            self._value = u""

        def write(self, message):
            try:
                self._value += message.decode("utf-8")
            except AttributeError:  # Already decoded
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
        sys.stdout = output

        # Pass the mock to the test
        result = func(obj, output)

        # Restore stdout
        sys.stdout = sys_stdout
        return result

    return wrapper


class TestEty(unittest.TestCase):
    def test_origins(self):
        word = ety.origins(ety.random_word())
        self.assertGreater(len(word), 0)

    def test_origins_recursion(self):
        o = ety.origins(ety.random_word(), recursive=True)
        self.assertGreater(len(o), 0)
        o = ety.origins("iland", recursive=True)
        self.assertGreater(len(o), 0)

    def test_lang(self):
        self.assertEqual(ety.Language("eng").name, "English")
        self.assertEqual(ety.Language("lat").name, "Latin")
        self.assertEqual(ety.Language("enm").name, "Middle English (1100-1500)")

    def test_lang_equal(self):
        a = ety.Language("eng")
        b = ety.Language("eng")
        c = ety.Language("lat")
        self.assertEqual(a, b)
        self.assertNotEqual(b, c)

    def test_word_equal(self):
        a = ety.Word("electronic")
        b = ety.Word("electronic", language="lat")
        c = ety.Word("electrinus")
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, c)

    def test_tree(self):
        self.assertGreaterEqual(len(str(ety.tree("aerodynamically")).split("\n")), 10)
        self.assertGreaterEqual(len(str(ety.tree("fabric")).split("\n")), 4)
        self.assertGreaterEqual(len(str(ety.tree("potato")).split("\n")), 2)

    def test_census_words(self):
        a = ety.census(["alphabet", "avocado", "guitar"])
        b = ety.census("alphabet avocado guitar")
        self.assertEqual(a, b)
        self.assertTrue(ety.Word("avocado") in a.words)
        with self.assertRaises(ValueError):
            ety.census(["valid", ety.Word("stillvalid"), 12345])

    def test_census_origins(self):
        a = ety.census("flying aerodynamically")
        b = ety.origins("flying")
        c = ety.origins("aerodynamically")

        self.assertEqual(a.origins(), b + c)

        d = ety.census("flying aerodynamically")
        e = ety.origins("flying", recursive=True)
        f = ety.origins("aerodynamically", recursive=True)

        self.assertEqual(d.origins(recursive=True), e + f)

    def test_word_len(self):
        word = ety.random_word().word
        self.assertEqual(len(ety.Word(word)), len(word))

    def test_tree_dict(self):
        self.assertIsInstance(ety.tree("potato").__dict__, dict)

    def test_nah_lang_code(self):
        tree = str(ety.tree("avocado"))
        self.assertTrue(tree.startswith("avocado (English)\n└── aguacate (Spanish)"))
        self.assertTrue("Nahuatl languages" in tree)

    @stdout_capture
    def test_cli_no_args(self, output):
        words = ["test"]
        sys.argv = ["ety.py", "test"]

        ety.cli()

        origins = ety.origins("test")

        expected_lines = len(words) + len(origins)

        self.assertEqual(expected_lines, output.lines)

    @stdout_capture
    def test_cli_recursive(self, output):
        words = ["test"]
        sys.argv = ["ety.py", "-r"] + words

        ety.cli()

        origins = ety.origins("test", recursive=True)

        expected_lines = len(words) + len(origins)

        self.assertEqual(expected_lines, output.lines)

    @stdout_capture
    def test_cli_tree(self, output):
        words = ["test"]
        sys.argv = ["ety.py", "-t"] + words

        ety.cli()

        tree = ety.tree("test")
        expected_lines = len(tree)

        self.assertEqual(expected_lines, output.lines)

    @stdout_capture
    def test_cli_multiple_words(self, output):
        words = ["test", "word"]
        sys.argv = ["ety.py"] + words

        ety.cli()

        origins = [origin for word in words for origin in ety.origins(word)]

        expected_lines = len(words) + len(origins) + len(words) - 1

        self.assertEqual(expected_lines, output.lines)

    @stdout_capture
    def test_cli_multiple_words_recursive(self, output):
        words = ["test", "word"]
        sys.argv = ["ety.py", "-r"] + words

        ety.cli()

        origins = [
            origin for word in words for origin in ety.origins(word, recursive=True)
        ]

        expected_lines = len(words) + len(origins) + len(words) - 1

        self.assertEqual(expected_lines, output.lines)

    @stdout_capture
    def test_cli_multiple_words_tree(self, output):
        words = ["test", "word"]
        sys.argv = ["ety.py", "-t"] + words

        ety.cli()

        trees = [ety.tree(word) for word in words]

        expected_length = sum(len(tree) for tree in trees) + len(words) - 1

        self.assertEqual(expected_length, output.lines)

    def test_format(self):
        from flake8.main.application import Application as Flake8

        linter = Flake8()

        linter.run(["."])

        self.assertEqual(linter.result_count, 0)


if __name__ == "__main__":
    unittest.main()
