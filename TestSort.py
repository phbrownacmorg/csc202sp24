import unittest
# import the code you want to test here
import random
from typing import TypeVar
from searchnsort import partition, quicksort

T = TypeVar('T')

class TestSort(unittest.TestCase):

    @staticmethod
    def is_sorted(array: list[T]) -> bool:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i+1]: # type: ignore
                sorted = False
        return sorted
    
    @staticmethod
    def is_partitioned(array: list[T], mid: int, start: int = 0, 
                       end: int = -100) -> bool:
        if end == -100:
            end = len(array)
        partitioned = True
        pivot = array[mid]
        for i in range(start, mid):
            if array[i] > pivot: # type: ignore
                partitioned = False
        for i in range(mid+1, end):
            if array[i] <= pivot: # type: ignore
                partitioned = False
        return partitioned

    def setUp(self) -> None:
        random.seed(385)

        self.__empty: list[int] = []
        self.__1: list[int] = [1]
        self.__2s: list[int] = list(range(2))
        self.__2u: list[int] = list(range(1, -1, -1))
        self.__9: list[int] = list(range(5)) + list(range(4))
        random.shuffle(self.__9)
        self.__10: list[int] = list(range(10))
        random.shuffle(self.__10)

    def testPartition2(self) -> None:
        self.assertEqual(partition(self.__2s, 0, 2), 0)
        self.assertEqual(self.__2s, [0, 1])
        self.assertEqual(partition(self.__2u, 0, 2), 1)
        self.assertEqual(self.__2u, [0, 1])

    def testPartition9(self) -> None:
        self.assertEqual(partition(self.__9, 0, 9), 1)
        self.assertTrue(TestSort.is_partitioned(self.__9, 1))

    def testPartition10(self) -> None:
        self.assertEqual(partition(self.__10, 0, 10), 8)
        self.assertTrue(TestSort.is_partitioned(self.__10, 8))

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptySorted(self) -> None:
        quicksort(self.__empty)
        self.assertTrue(TestSort.is_sorted(self.__empty))

    def testSorted1(self) -> None:
        quicksort(self.__1)
        self.assertTrue(TestSort.is_sorted(self.__1))

    def testSort2s(self) -> None:
        self.assertTrue(TestSort.is_sorted(self.__2s))
        quicksort(self.__2s)
        self.assertTrue(TestSort.is_sorted(self.__2s))

    def testSort2u(self) -> None:
        self.assertFalse(TestSort.is_sorted(self.__2u))
        quicksort(self.__2u)
        self.assertTrue(TestSort.is_sorted(self.__2u))

    def testSort9(self) -> None:
        self.assertFalse(TestSort.is_sorted(self.__9))
        quicksort(self.__9)
        self.assertTrue(TestSort.is_sorted(self.__9))

    # @unittest.skip('')
    def testSort10(self) -> None:
        self.assertFalse(TestSort.is_sorted(self.__10))
        quicksort(self.__10)
        self.assertTrue(TestSort.is_sorted(self.__10))


if __name__ == '__main__':
    unittest.main()

