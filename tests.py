import unittest
import ety


class TestEty(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_origins(self):
        o = ety.origins(ety.random_word())
        self.assertGreater(len(o), 0)

    def test_lang(self):
        self.assertEqual(ety.lang_name('eng'), 'English')
        self.assertEqual(ety.lang_name('lat'), 'Latin')
        self.assertEqual(ety.lang_name('enm'), 'Middle English (1100-1500)')

    def test_tree(self):
        self.assertGreaterEqual(len(str(
            ety.tree('aerodynamically')).split('\n')), 10)
        self.assertGreaterEqual(len(str(
            ety.tree('fabric')).split('\n')), 4)


if __name__ == '__main__':
    unittest.main()
