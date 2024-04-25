import unittest
# import the code you want to test here
from BinTree import BinTree

class TestBinTree(unittest.TestCase):

    def setUp(self) -> None:
        self.__empty = BinTree[str]() # type: ignore

        self.__1 = BinTree[str]() # type: ignore
        self.__1._data = 'Tabitha' # 1-node tree

        self.__4 = BinTree[str]() # type: ignore
        self.__4._data = 'Ariel'
        self.__4._left = BinTree[str]('Ariana')
        self.__4._right = BinTree[str]('Luci')
        self.__4._right._left = BinTree[str]('Elliott') # 4-node tree

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptyTrue(self) -> None:
        self.assertTrue(self.__empty.empty())

    def testEmptyFalse(self) -> None:
        self.assertFalse(self.__1.empty())
        self.assertFalse(self.__4.empty())

    def testData(self) -> None:
        with self.assertRaises(AssertionError):
            self.__empty.data()
        self.assertEqual(self.__1.data(), 'Tabitha')
        self.assertEqual(self.__4.data(), 'Ariel')
        self.assertEqual(self.__4._left.data(), 'Ariana')
        self.assertEqual(self.__4._right.data(), 'Luci')
        self.assertEqual(self.__4._right._left.data(), 'Elliott')

    def testLen(self) -> None:
        self.assertEqual(len(self.__empty), 0)
        self.assertEqual(len(self.__1), 1)
        self.assertEqual(len(self.__4), 4)

    def testHeight(self) -> None:
        self.assertEqual(self.__empty.height(), 0)
        self.assertEqual(self.__1.height(), 1)
        self.assertEqual(self.__4.height(), 3)

    def testPreorder(self) -> None:
        self.assertEqual(self.__empty.preorder(), [])
        self.assertEqual(self.__1.preorder(), ['Tabitha'])
        self.assertEqual(self.__4.preorder(), ['Ariel', 'Ariana', 'Luci', 'Elliott'])

    def testPostorder(self) -> None:
        self.assertEqual(self.__empty.postorder(), [])
        self.assertEqual(self.__1.postorder(), ['Tabitha'])
        self.assertEqual(self.__4.postorder(), ['Ariana', 'Elliott', 'Luci', 'Ariel'])

    def testInorder(self) -> None:
        self.assertEqual(self.__empty.inorder(), [])
        self.assertEqual(self.__1.inorder(), ['Tabitha'])
        self.assertEqual(self.__4.inorder(), ['Ariana', 'Ariel', 'Elliott', 'Luci'])



    # def testIndex(self) -> None:
    #     with self.assertRaises(ValueError):
    #         self.__empty.index(1)
    #     self.assertEqual(self.__1.index(1), 0)
    #     with self.assertRaises(ValueError):
    #         self.__1.index(2)
    #     for i in range(1, 5):
    #         with self.subTest(i=i):
    #             self.assertEqual(self.__4.index(i), 4-i)
    #     with self.assertRaises(ValueError):
    #         self.__1.index(5)
        
    # def testPopEmpty(self) -> None:
    #     with self.assertRaises(IndexError):
    #         self.__empty.pop()

    # def testPop_1_1(self) -> None:
    #     with self.assertRaises(IndexError):
    #         self.__1.pop(1) # Too big

    # def testPop_1_n2(self) -> None:
    #     with self.assertRaises(IndexError):
    #         self.__1.pop(-2) # Too small

    # def testPop_1_0(self) -> None:
    #     self.assertEqual(self.__1.pop(0), 1)
    #     self.assertTrue(self.__1.empty())

    # def testPop_1_n1(self) -> None:
    #     self.assertEqual(self.__1.pop(-1), 1)
    #     self.assertTrue(self.__1.empty())

    # def testPop_4_4(self) -> None:
    #     with self.assertRaises(IndexError):
    #         self.__4.pop(4) # Too big

    # def testPop_4_n5(self) -> None:
    #     with self.assertRaises(IndexError):
    #         self.__4.pop(-5) # Too small

    # def testPop_4_0(self) -> None:
    #     self.assertEqual(self.__4.pop(0), 4)
    #     self.assertEqual(str(self.__4), '❬3❭➞❬2❭➞❬1❭➞∅')

    # def testPop_4_3(self) -> None:
    #     self.assertEqual(self.__4.pop(3), 1)
    #     self.assertEqual(str(self.__4), '❬4❭➞❬3❭➞❬2❭➞∅')

    # def testPop_4_n1(self) -> None:
    #     self.assertEqual(self.__4.pop(), 1)
    #     self.assertEqual(str(self.__4), '❬4❭➞❬3❭➞❬2❭➞∅')

    # def testPop_4_n4(self) -> None:
    #     self.assertEqual(self.__4.pop(-4), 4)
    #     self.assertEqual(str(self.__4), '❬3❭➞❬2❭➞❬1❭➞∅')

    # def testPop_4_2(self) -> None:
    #     self.assertEqual(self.__4.pop(2), 2)
    #     self.assertEqual(str(self.__4), '❬4❭➞❬3❭➞❬1❭➞∅')

    # def testPop_4_n3(self) -> None:
    #     self.assertEqual(self.__4.pop(-3), 3)
    #     self.assertEqual(str(self.__4), '❬4❭➞❬2❭➞❬1❭➞∅')


if __name__ == '__main__':
    unittest.main()

