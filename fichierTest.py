import codeAtester as ex
import unittest
from math import pi
from hypothesis import given
import hypothesis.strategies as st


class testEx1(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test_positif(self, x, y):
        self.assertEqual(ex.exercice_1(x,y), x*y)

class testEx2(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test_positif(self, x, y):
        self.assertEqual(ex.exercice_1(x,y), x*y)


class testEx3(unittest.TestCase):

    def test_init(self):
        self.assertGreaterEqual(2, 0)


if __name__ == '__main__':
    unittest.main()