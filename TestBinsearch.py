import unittest
# import the code you want to test here
from searchnsort import binsearch

class TestBinsearch(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testTrue(self) -> None:
        self.assertTrue(binsearch(10, list(range(0, 20, 2))))

    def testEarly(self) -> None:
        self.assertTrue(binsearch(0, list(range(0, 20, 2))))

    def testLate(self) -> None:
        self.assertTrue(binsearch(18, list(range(0, 20, 2))))

    def testAbsent(self) -> None:
        self.assertFalse(binsearch(11, list(range(0, 20, 2))))


if __name__ == '__main__':
    unittest.main()

