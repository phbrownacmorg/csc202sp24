import unittest
# import the code you want to test here
from Stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.empty = Stack[int]() # type: ignore

        self._1 = Stack[int]() # type: ignore
        self._1.push(7)

        self._4 = Stack[int]() # type: ignore
        self._4.push(4)
        self._4.push(9)
        self._4.push(3)
        self._4.push(2)

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptyTrue(self) -> None:
        self.assertTrue(self.empty.empty())

    def testPushOne(self) -> None:
        self.assertTrue(self.empty.empty())
        self.empty.push(7)
        self.assertFalse(self.empty.empty())
        self.assertEqual(self.empty.peek(), 7)

    def testPop4(self) -> None:
        self.assertFalse(self._4.empty())
        self.assertEqual(self._4.pop(), 2)
        self.assertEqual(self._4.pop(), 3)
        self.assertEqual(self._4.pop(), 9)
        self.assertEqual(self._4.pop(), 4)
        self.assertTrue(self._4.empty())

    def testPopOne(self) -> None:
        self.assertFalse(self._1.empty())
        self.assertEqual(self._1.peek(), 7)
        self.assertEqual(self._1.pop(), 7)
        self.assertTrue(self._1.empty())

if __name__ == '__main__':
    unittest.main()

