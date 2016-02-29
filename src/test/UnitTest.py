import unittest
from myfunctions import my_contains, my_first


# subclass unittest.TestCase
class Test(unittest.TestCase):
    """in here we are testing that 1 + 1 is always 2
    `   the function name must beging with test_
    """

    def test_basic_addition(self):
        self.failUnlessEqual(1 + 1, 2)


class TestMyFunctions(unittest.TestCase):
    def test_contains_simple_true(self):
        self.assertTrue(my_contains(3, [1, 2, 3]))

    def test_first_number(self):
        self.assertTrue(my_first([1, 2, 3]), 1)


if __name__ == '__main__':
    unittest.main()
