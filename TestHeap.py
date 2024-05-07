import unittest
# import the code you want to test here
from Heap import Heap

class TestHeap(unittest.TestCase):

    def setUp(self) -> None:
        self._empty = Heap[int]()

        self._1 = Heap[int]()
        self._1.add(17)

        self._4 = Heap[int]()
        self._4.add(32)
        self._4.add(23)
        self._4.add(4)
        self._4.add(58)

        self._7 = Heap[int]()
        self._7.add(32)
        self._7.add(23)
        self._7.add(4)
        self._7.add(58)
        self._7.add(14)
        self._7.add(9)
        self._7.add(21)

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptyTrue(self) -> None:
        self.assertTrue(self._empty.empty())

    def testEmptyFalse(self) -> None:
        self.assertFalse(self._1.empty())
        self.assertFalse(self._4.empty())
        self.assertFalse(self._7.empty())

    def testLen0(self) -> None:
        self.assertEqual(len(self._empty), 0)

    def testLen1(self) -> None:
        self.assertEqual(len(self._1), 1)

    def testLen4(self) -> None:
        self.assertEqual(len(self._4), 4)

    def testLen7(self) -> None:
        self.assertEqual(len(self._7), 7)

    def testPeekPre(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.peek()

    def testPeek1(self) -> None:
        self.assertEqual(self._1.peek(), 17)

    def testPeek4(self) -> None:
        self.assertEqual(self._4.peek(), 58)

    def testPeek7(self) -> None:
        self.assertEqual(self._7.peek(), 58)

    def testPopPre(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.pop()

    def testPop1(self) -> None:
        self.assertEqual(self._1.pop(), 17)
        self.assertEqual(len(self._1), 0)

    def testPop4(self) -> None:
        self.assertEqual(self._4.pop(), 58)
        self.assertEqual(len(self._4), 3)
        self.assertEqual(self._4.pop(), 32)
        self.assertEqual(len(self._4), 2)
        self.assertEqual(self._4.pop(), 23)
        self.assertEqual(len(self._4), 1)
        self.assertEqual(self._4.pop(), 4)
        self.assertEqual(len(self._4), 0)

    def testPop7(self) -> None:
        self.assertEqual(self._7.pop(), 58)
        self.assertEqual(len(self._7), 6)
        self.assertEqual(self._7.pop(), 32)
        self.assertEqual(len(self._7), 5)
        self.assertEqual(self._7.pop(), 23)
        self.assertEqual(len(self._7), 4)
        self.assertEqual(self._7.pop(), 21)
        self.assertEqual(len(self._7), 3)
        self.assertEqual(self._7.pop(), 14)
        self.assertEqual(len(self._7), 2)
        self.assertEqual(self._7.pop(), 9)
        self.assertEqual(len(self._7), 1)
        self.assertEqual(self._7.pop(), 4)
        self.assertEqual(len(self._7), 0)


if __name__ == '__main__':
    unittest.main()

