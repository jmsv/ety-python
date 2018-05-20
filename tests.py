import unittest
import ety


class TestEty(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_lang(self):
        self.assertEqual(ety.lang_name('eng'), 'English')


if __name__ == '__main__':
    print(ety.origins('car'))
    for origin in (ety.origins('car', recursive=True)):
        print(ety.lang_name(origin['lang']))
    print(ety.random_word())
    unittest.main()
