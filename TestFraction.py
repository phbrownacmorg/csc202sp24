import unittest
# import the code you want to test here
from Fraction import Fraction

class TestFraction(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testInvariant_1_2(self) -> None:
        self.assertTrue(Fraction(1, 2)._invariant())

    def testInvariant_5_2(self) -> None:
        self.assertTrue(Fraction(5, 2)._invariant())

    def testInvariant_m1_2(self) -> None:
        self.assertTrue(Fraction(-1, 2)._invariant())

    def testInvariant_m1_m2(self) -> None:
        self.assertTrue(Fraction(-1, -2)._invariant())

    def testInvariant_12_24(self) -> None:
        self.assertTrue(Fraction(12, 24)._invariant())

    def testInvariant_1_0(self) -> None:
        with self.assertRaises(AssertionError) as cm:
            Fraction(1, 0)
        xc = cm.exception
        self.assertEqual(xc.args[0], "Denominator cannot be 0")
    
    def testStr_1_2(self) -> None:
        self.assertEqual(str(Fraction(1, 2)), '1/2')

    def testStr_5_2(self) -> None:
        self.assertEqual(str(Fraction(5, 2)), '5/2')

    def testStr_m1_2(self) -> None:
        self.assertEqual(str(Fraction(-1, 2)), '-1/2')

    def testStr_m1_m2(self) -> None:
        self.assertEqual(str(Fraction(-1, -2)), '1/2')

    def testStr_12_24(self) -> None:
        self.assertEqual(str(Fraction(12, 24)), '1/2')

    def testNum_1_2(self) -> None:
        self.assertEqual(Fraction(1, 2).getNumr(), 1)

    def testNum_5_2(self) -> None:
        self.assertEqual(Fraction(5, 2).getNumr(), 5)

    def testNum_m1_2(self) -> None:
        self.assertEqual(Fraction(-1, 2).getNumr(), -1)

    def testDenom_1_2(self) -> None:
        self.assertEqual(Fraction(1, 2).getDenom(), 2)

    def testDenom_m1_m2(self) -> None:
        self.assertEqual(Fraction(-1, -2).getDenom(), 2)

    def testDenom_12_24(self) -> None:
        self.assertEqual(Fraction(12, 24).getDenom(), 2)

    def testEq_1_2_1_2(self) -> None:
        self.assertTrue(Fraction(1, 2) == Fraction(1, 2))

    def testEq_1_2_3_6(self) -> None:
        self.assertTrue(Fraction(1, 2) == Fraction(3, 6))

    def testEq_n8_36_2_n9(self) -> None:
        self.assertTrue(Fraction(-8, 36) == Fraction(2, -9))

    def testEq_same_num(self) -> None:
        self.assertFalse(Fraction(2, 3) == Fraction(2, 5))

    def testEq_same_denom(self) -> None:
        self.assertFalse(Fraction(3, 5) == Fraction(2, 5))

    def testEq_both_differ(self) -> None:
        self.assertFalse(Fraction(2, 3) == Fraction(3, 4))

    def testAdd_halves(self) -> None:
        self.assertTrue(Fraction(1, 1) == 
            Fraction(1, 2) + Fraction(512, 1024))

    def testAdd_1_3_1_2(self) -> None:
        # Note assertEqual uses our __eq__ method
        self.assertEqual(Fraction(5, 6), Fraction(1, 3) + Fraction(1, 2))

    def testAdd_1_3_n1_2(self) -> None:
        # Note assertEqual uses our __eq__ method
        self.assertEqual(Fraction(-1, 6), Fraction(1, 3) + Fraction(-1, 2))


if __name__ == '__main__':
    unittest.main()

