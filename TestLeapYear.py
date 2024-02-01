import unittest
# import the code you want to test here
from leapyear import *

class TestLeapYear(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testJulianLeapYear(self) -> None:
        self.assertTrue(is_leap_year(2024))

    def testJulianNonLeapYear(self) -> None:
        self.assertFalse(is_leap_year(2023))
        self.assertFalse(is_leap_year(2022))
        self.assertFalse(is_leap_year(2021))

    def testGregorianCenturyYear(self) -> None:
        self.assertFalse(is_leap_year(1900))

    def testGregorian400Year(self) -> None:
        self.assertTrue(is_leap_year(2000))

    def testPrecondition(self) -> None:
        with self.assertRaises(AssertionError) as cm:
            is_leap_year(1500)
        xc = cm.exception
        self.assertEqual(xc.args[0], "Year is pre-Gregorian")

if __name__ == '__main__':
    unittest.main()

