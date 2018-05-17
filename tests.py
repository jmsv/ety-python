import unittest
import ety
import re


class TestEty(unittest.TestCase):

    def test_origins_returns_list(self):
        origins = ety.origins('potato')
        self.assertIsInstance(origins, list)
        self.assertGreater(len(origins), 1)

    def test_words_returns_list(self):
        origins = ety.words('taino')
        self.assertIsInstance(origins, list)
        self.assertGreater(len(origins), 5)

    def test_random_word(self):
        for _ in range(10):
            word = ety.random_word()
            self.assertIsNotNone(re.match(r'^(\w|.|-)+$', word))


if __name__ == '__main__':
    unittest.main()
