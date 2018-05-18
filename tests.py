import unittest
import ety


class TestEty(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)


if __name__ == '__main__':
    print(ety.origins('car'))
    print(ety.random_word())
    unittest.main()
