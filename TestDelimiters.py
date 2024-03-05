import unittest
# import the code you want to test here
from balanced_delimiters import balanced

class TestDelimiters(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmpty(self) -> None:
        self.assertTrue(balanced(''))

    def testParens(self) -> None:
        self.assertTrue(balanced('()'))

    def testBrackets(self) -> None:
        self.assertTrue(balanced('[]'))

    def testBraces(self) -> None:
        self.assertTrue(balanced('{}'))

    def testMismatches(self) -> None:
        self.assertFalse(balanced('(]'))
        self.assertFalse(balanced('(}'))
        self.assertFalse(balanced('{]'))
        self.assertFalse(balanced('{)'))
        self.assertFalse(balanced('[}'))
        self.assertFalse(balanced('[)'))

    def testCombinations(self) -> None:
        self.assertTrue(balanced('({[]})'))
        self.assertTrue(balanced('([{}])'))
        self.assertTrue(balanced('{[()]}'))
        self.assertTrue(balanced('[{()}]'))
        self.assertTrue(balanced('(){}[]'))
        self.assertTrue(balanced('(){[]}'))
        self.assertTrue(balanced('({})[]'))

    def testMisordered(self) -> None:
        self.assertFalse(balanced('({[}])'))
        self.assertFalse(balanced('({[]}]'))
        self.assertFalse(balanced('(){)[]'))
        self.assertFalse(balanced('({])[]'))
        self.assertFalse(balanced('({}}[]'))

    def testStackIssues(self) -> None:
        self.assertFalse(balanced('({[]}'))
        self.assertFalse(balanced('({})]['))

    def testExpr(self) -> None:
        self.assertTrue(balanced('[((1 + 3) * 2) / ((4 - 7) + 18)]'))
        self.assertFalse(balanced('[((1 + 3) * 2) / ((4 - 7) + 18)'))
        self.assertFalse(balanced('[((1 + 3) * 2 / ((4 - 7) + 18)]'))
        self.assertFalse(balanced('[((1 + 3) * 2) / ({4 - 7) + 18)]'))
        self.assertFalse(balanced('(((1 + 3)) * 2)) / ((4 - 7) + 18))'))

if __name__ == '__main__':
    unittest.main()

