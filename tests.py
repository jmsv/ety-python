import unittest
import ety


class TestEty(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_lang(self):
        self.assertEqual(ety.lang_name('eng'), 'English')
        self.assertEqual(ety.lang_name('lat'), 'Latin')
        self.assertEqual(ety.lang_name('enm'), 'Middle English (1100-1500)')


if __name__ == '__main__':
    unittest.main()
