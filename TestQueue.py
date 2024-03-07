import unittest
# import the code you want to test here
#from Queue import Queue
#from CircQ import Queue
from Q2Stacks import Queue

class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self._empty = Queue[int]()

        self._1 = Queue[int]()
        self._1.add(7)

        self._4 = Queue[int]()
        self._4.add(4)
        self._4.add(9)
        self._4.add(3)
        self._4.add(2)

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptyTrue(self) -> None:
        self.assertTrue(self._empty.empty())

    def testPeekPre(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.peek()

    def testAddOne(self) -> None:
        self.assertTrue(self._empty.empty())
        self._empty.add(7)
        self.assertFalse(self._empty.empty())
        self.assertEqual(self._empty.peek(), 7)

    def testPopPre(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.pop()

    def testPop4(self) -> None:
        self.assertFalse(self._4.empty())
        self.assertEqual(self._4.pop(), 4)
        self.assertEqual(self._4.pop(), 9)
        self.assertEqual(self._4.pop(), 3)
        self.assertEqual(self._4.pop(), 2)
        self.assertTrue(self._4.empty())

    def testPopOne(self) -> None:
        self.assertFalse(self._1.empty())
        self.assertEqual(self._1.peek(), 7)
        self.assertEqual(self._1.pop(), 7)
        self.assertTrue(self._1.empty())

    def testWraparound(self) -> None:
        """Basically here to verify the correct wrapping of
        the head and tail indices in CircQ, but the tests will
        work correctly for other implementations as well."""
        # Make some space in self.__items[0:1]
        self.assertEqual(self._4.pop(), 4)
        self.assertEqual(self._4.pop(), 9)
        # Did self.__tail wrap around correctly?
        self._4.add(5)
        self._4.add(7)
        # Does self.__head wrap around correctly?
        self.assertEqual(self._4.pop(), 3)
        self.assertEqual(self._4.pop(), 2)
        self.assertEqual(self._4.pop(), 5)
        self.assertEqual(self._4.pop(), 7)
        self.assertTrue(self._4.empty())

    def testResize(self) -> None:
        """Basically here to test correct resizing of the queue
        in CircQ, but the tests will work correctly for other
        implementations as well."""
        self._4.add(5)
        self._4.add(7)
        self.assertFalse(self._4.empty())
        self.assertEqual(self._4.pop(), 4)
        self.assertEqual(self._4.pop(), 9)
        self.assertEqual(self._4.pop(), 3)
        self.assertEqual(self._4.pop(), 2)
        self.assertEqual(self._4.pop(), 5)
        self.assertEqual(self._4.pop(), 7)
        self.assertTrue(self._4.empty())

if __name__ == '__main__':
    unittest.main()

