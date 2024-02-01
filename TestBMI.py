import unittest
# import the code you want to test here
from BMI import *

class TestBMI(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test

    # calc_BMI is a continuous function on the positive real numbers
    # (both arguments > 0).  Try enough points to make sure we're talking
    # about the same curve.
    def testCalc_h10_w1(self) -> None:
        self.assertAlmostEqual(calc_bmi(10, 1), 7.03)

    def testCalc_h60_w100(self) -> None:
        self.assertAlmostEqual(calc_bmi(60, 100), 19.52777778)

    def testCalc_Shaq(self) -> None:
        self.assertAlmostEqual(calc_bmi(85, 325), 31.62283737)

    def testCalc_avg_American_woman(self) -> None:
        self.assertAlmostEqual(calc_bmi(63.5, 170.8), 29.7780148)

    # Inputs to classify_bmi group into classes.  For each group,
    # test top and bottom boundary cases and representative case
    def testClassify_underweight_bottom(self) -> None:
        self.assertEqual(classify_bmi(0.0001), 'underweight')

    def testClassify_underweight_middle(self) -> None:
        self.assertEqual(classify_bmi(15), 'underweight')

    def testClassify_underweight_top(self) -> None:
        self.assertEqual(classify_bmi(18.499999), 'underweight')

    def testClassify_normal_bottom(self) -> None:
        self.assertEqual(classify_bmi(18.5), 'normal')

    def testClassify_normal_middle(self) -> None:
        self.assertEqual(classify_bmi(22), 'normal')

    def testClassify_normal_top(self) -> None:
        self.assertEqual(classify_bmi(24.999999), 'normal')

    def testClassify_overweight_bottom(self) -> None:
        self.assertEqual(classify_bmi(25), 'overweight')

    def testClassify_overweight_middle(self) -> None:
        self.assertEqual(classify_bmi(28), 'overweight')

    def testClassify_overweight_top(self) -> None:
        self.assertEqual(classify_bmi(29.999999), 'overweight')

    def testClassify_obese_bottom(self) -> None:
        self.assertEqual(classify_bmi(30), 'obese')

    def testClassify_obese_middle(self) -> None:
        self.assertEqual(classify_bmi(33), 'obese')

    # No top boundary for obese

if __name__ == '__main__':
    unittest.main()

