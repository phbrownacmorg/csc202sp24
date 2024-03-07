import unittest
# import the code you want to test here
from palindrome_stack_queue import palindrome

class TestPalindrome(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testTrue(self) -> None:
        self.assertTrue(palindrome(''))

    def test1Char(self) -> None:
        self.assertTrue(palindrome('I'))

    def testABBA(self) -> None:
        self.assertTrue(palindrome('ABBA'))

    def testAbby(self) -> None:
        self.assertFalse(palindrome('Abby'))

    def testHannah(self) -> None:
        self.assertTrue(palindrome('Hannah'))

    def testNathan(self) -> None:
        self.assertFalse(palindrome('Nathan'))

    def testNathanThorn(self) -> None:
        self.assertTrue(palindrome('Na\u00fean'))

    def testMadam(self) -> None:
        self.assertTrue(palindrome("Madam, I'm Adam."))

    def testTR(self) -> None:
        self.assertTrue(palindrome("A man, a plan, a canal: Panama!"))


if __name__ == '__main__':
    unittest.main()

