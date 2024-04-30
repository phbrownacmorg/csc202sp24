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


        self.__7 = BinTree[str]('Jay')
        self.__7._left = BinTree['str']('Ariel')
        self.__7._right = BinTree[str]('Tabitha')
        self.__7._left._left = BinTree[str]('Ariana')
        self.__7._left._right = BinTree[str]('Khushi')
        self.__7._right._left = BinTree[str]('Luci')
        self.__7._right._right = BinTree[str]('Zariyah')

        self.__15 = BinTree[str]('Jay')
        self.__15._left = BinTree['str']('Ariel')
        self.__15._right = BinTree[str]('Tabitha')
        self.__15._left._left = BinTree[str]('Ariana')
        self.__15._left._right = BinTree[str]('Khushi')
        self.__15._right._left = BinTree[str]('Luci')
        self.__15._right._right = BinTree[str]('Zariyah')
        self.__15._left._left._left = BinTree[str]('Nathan')
        self.__15._left._left._right = BinTree[str]('Caleb D.')
        self.__15._left._right._left = BinTree[str]('Caleb M.')
        self.__15._left._right._right = BinTree[str]('Marco')
        self.__15._right._left._left = BinTree[str]('Elliott')
        self.__15._right._left._right = BinTree[str]('Skyler')
        self.__15._right._right._left = BinTree[str]('Trig')
        self.__15._right._right._right = BinTree[str]('Tyson')

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
        self.assertEqual(self.__4.left().data(), 'Ariana')
        self.assertEqual(self.__4.right().data(), 'Luci')
        self.assertEqual(self.__4.right().left().data(), 'Elliott')

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
        self.assertEqual(self.__7.preorder(), ['Jay', 'Ariel', 'Ariana', 'Khushi',
                                               'Tabitha', 'Luci', 'Zariyah'])

    def testPostorder(self) -> None:
        self.assertEqual(self.__empty.postorder(), [])
        self.assertEqual(self.__1.postorder(), ['Tabitha'])
        self.assertEqual(self.__4.postorder(), ['Ariana', 'Elliott', 'Luci', 'Ariel'])
        self.assertEqual(self.__7.postorder(), ['Ariana', 'Khushi', 'Ariel', 'Luci',
                                                'Zariyah', 'Tabitha', 'Jay'])

    def testInorder(self) -> None:
        self.assertEqual(self.__empty.inorder(), [])
        self.assertEqual(self.__1.inorder(), ['Tabitha'])
        self.assertEqual(self.__4.inorder(), ['Ariana', 'Ariel', 'Elliott', 'Luci'])
        self.assertEqual(self.__7.inorder(), ['Ariana', 'Ariel', 'Khushi', 'Jay',
                                              'Luci', 'Tabitha', 'Zariyah'])

    def testPreorderBreadthFirst(self) -> None:
        self.assertEqual(self.__empty.preorderBreadthFirst(), [])
        self.assertEqual(self.__1.preorderBreadthFirst(), ['Tabitha'])
        self.assertEqual(self.__4.preorderBreadthFirst(), 
                         ['Ariel', 'Ariana', 'Luci', 'Elliott'])
        self.assertEqual(self.__7.preorderBreadthFirst(),
                         ['Jay', 'Ariel', 'Tabitha', 'Ariana', 'Khushi', 'Luci', 'Zariyah'])

    def testPostorderBreadthFirst(self) -> None:
        self.assertEqual(self.__empty.postorderBreadthFirst(), [])
        self.assertEqual(self.__1.postorderBreadthFirst(), ['Tabitha'])
        self.assertEqual(self.__4.postorderBreadthFirst(), 
                         ['Elliott', 'Ariana', 'Luci', 'Ariel'])
        self.assertEqual(self.__7.postorderBreadthFirst(),
                         ['Ariana', 'Khushi', 'Luci', 'Zariyah', 'Ariel', 'Tabitha', 'Jay'])
        self.assertEqual(self.__15.postorderBreadthFirst(),
                         ['Nathan', 'Caleb D.', 'Caleb M.', 'Marco', 
                          'Elliott', 'Skyler', 'Trig', 'Tyson',
                          'Ariana', 'Khushi', 'Luci', 'Zariyah', 
                          'Ariel', 'Tabitha', 'Jay'])



if __name__ == '__main__':
    unittest.main()

