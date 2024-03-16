import unittest
# import the code you want to test here
from LList import LList

class TestLList(unittest.TestCase):

    def setUp(self) -> None:
        self.__empty = LList[int]() # type: ignore

        self.__1 = LList[int]() # type: ignore 
        self.__1.add(1)         # 1-node list

        self.__4 = LList[int]() # type: ignore
        self.__4.add(1)
        self.__4.add(2)
        self.__4.add(3)
        self.__4.add(4)         # 4-node list

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptyTrue(self) -> None:
        self.assertTrue(self.__empty.empty())

    def testEmptyFalse(self) -> None:
        self.assertFalse(self.__1.empty())
        self.assertFalse(self.__4.empty())

    def testValue(self) -> None:
        self.assertEqual(self.__1.value(), 1)
        self.assertEqual(self.__4.value(), 4)
        with self.assertRaises(AssertionError):
            self.__empty.value()

    def testNext(self) -> None:
        self.assertTrue(self.__1.next().empty())
        self.assertTrue(self.__4.next().value(), 3)
        self.assertTrue(self.__4.next().next().value(), 2)
        self.assertTrue(self.__4.next().next().next().value(), 1)
        with self.assertRaises(AssertionError):
            self.__empty.next()

    def testLen(self) -> None:
        self.assertEqual(len(self.__empty), 0)
        self.assertEqual(len(self.__1), 1)
        self.assertEqual(len(self.__4), 4)

    def testStr(self) -> None:
        self.assertEqual(str(self.__empty), '∅')
        self.assertEqual(str(self.__1), '❬1❭➞∅')
        self.assertEqual(str(self.__4), '❬4❭➞❬3❭➞❬2❭➞❬1❭➞∅')

    def testIndex(self) -> None:
        with self.assertRaises(ValueError):
            self.__empty.index(1)
        self.assertEqual(self.__1.index(1), 0)
        with self.assertRaises(ValueError):
            self.__1.index(2)
        for i in range(1, 5):
            with self.subTest(i=i):
                self.assertEqual(self.__4.index(i), 4-i)
        with self.assertRaises(ValueError):
            self.__1.index(5)
        
    def testPopEmpty(self) -> None:
        with self.assertRaises(IndexError):
            self.__empty.pop()

    def testPop_1_1(self) -> None:
        with self.assertRaises(IndexError):
            self.__1.pop(1) # Too big

    def testPop_1_n2(self) -> None:
        with self.assertRaises(IndexError):
            self.__1.pop(-2) # Too small

    def testPop_1_0(self) -> None:
        self.assertEqual(self.__1.pop(0), 1)
        self.assertTrue(self.__1.empty())

    def testPop_1_n1(self) -> None:
        self.assertEqual(self.__1.pop(-1), 1)
        self.assertTrue(self.__1.empty())

    def testPop_4_4(self) -> None:
        with self.assertRaises(IndexError):
            self.__4.pop(4) # Too big

    def testPop_4_n5(self) -> None:
        with self.assertRaises(IndexError):
            self.__4.pop(-5) # Too small

    def testPop_4_0(self) -> None:
        self.assertEqual(self.__4.pop(0), 4)
        self.assertEqual(str(self.__4), '❬3❭➞❬2❭➞❬1❭➞∅')

    def testPop_4_3(self) -> None:
        self.assertEqual(self.__4.pop(3), 1)
        self.assertEqual(str(self.__4), '❬4❭➞❬3❭➞❬2❭➞∅')

    def testPop_4_n1(self) -> None:
        self.assertEqual(self.__4.pop(), 1)
        self.assertEqual(str(self.__4), '❬4❭➞❬3❭➞❬2❭➞∅')

    def testPop_4_n4(self) -> None:
        self.assertEqual(self.__4.pop(-4), 4)
        self.assertEqual(str(self.__4), '❬3❭➞❬2❭➞❬1❭➞∅')

    def testPop_4_2(self) -> None:
        self.assertEqual(self.__4.pop(2), 2)
        self.assertEqual(str(self.__4), '❬4❭➞❬3❭➞❬1❭➞∅')

    def testPop_4_n3(self) -> None:
        self.assertEqual(self.__4.pop(-3), 3)
        self.assertEqual(str(self.__4), '❬4❭➞❬2❭➞❬1❭➞∅')


if __name__ == '__main__':
    unittest.main()

