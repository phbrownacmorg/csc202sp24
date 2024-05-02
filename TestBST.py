import unittest
# import the code you want to test here
from BST import BST

class TestBST(unittest.TestCase):

    def setUp(self) -> None:
        self.__empty = BST[str]() # type: ignore

        # 1-node tree
        self.__1 = BST[str]('Tabitha') # type: ignore

        # 4-node tree
        self.__4 = BST[str]('Ariel') # type: ignore
        self.__4.add('Ariana')
        self.__4.add('Luci')
        self.__4.add('Elliott')

        self.__7 = BST[str]('Khushi')
        self.__7.add('Ariel')
        self.__7.add('Tabitha')
        self.__7.add('Ariana')
        self.__7.add('Jay')
        self.__7.add('Luci')
        self.__7.add('Zariyah')

        self.__15 = BST[str]('Khushi')
        self.__15.add('Ariel')
        self.__15.add('Tabitha')
        self.__15.add('Ariana')
        self.__15.add('Jay')
        self.__15.add('Luci')
        self.__15.add('Zariyah')
        self.__15.add('Caleb M.')
        self.__15.add('Caleb D.')
        self.__15.add('Elliott')
        self.__15.add('Nathan')
        self.__15.add('Marco')
        self.__15.add('Skyler')
        self.__15.add('Trig')
        self.__15.add('Tyson')

        self._present_values = self.__15.preorderBreadthFirst()
        self._absent_values = ['Alice', 'Arid', 'Brandon', 'Caleb E.', 'Daniel', 
                               'Grayson', 'Kennedy', 'Laura', 'Lydia', 'Maggie', 
                               'Olivia', 'Stirling', 'Tom', 'Tucker', 'Washington',
                               'Zelda']

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def test4Structure(self) -> None:
        self.assertEqual(self.__4.preorder(), ['Ariel', 'Ariana', 'Luci', 'Elliott'])
        self.assertEqual(self.__4.postorder(), ['Ariana', 'Elliott', 'Luci', 'Ariel'])
        self.assertEqual(self.__4.inorder(), ['Ariana', 'Ariel', 'Elliott', 'Luci'])
        self.assertEqual(self.__4.postorderBreadthFirst(), 
                         ['Elliott', 'Ariana', 'Luci', 'Ariel'])
        self.assertEqual(self.__4.data(), 'Ariel')
        self.assertEqual(self.__4.left().data(), 'Ariana')
        self.assertEqual(self.__4.right().data(), 'Luci')
        self.assertEqual(self.__4.right().left().data(), 'Elliott')

    def test7Structure(self) -> None:
        self.assertEqual(self.__7.preorder(), ['Khushi', 'Ariel', 'Ariana', 'Jay',
                                               'Tabitha', 'Luci', 'Zariyah'])
        self.assertEqual(self.__7.postorder(), ['Ariana', 'Jay', 'Ariel', 'Luci',
                                                'Zariyah', 'Tabitha', 'Khushi'])
        self.assertEqual(self.__7.inorder(), ['Ariana', 'Ariel', 'Jay', 'Khushi',
                                              'Luci', 'Tabitha', 'Zariyah'])
        self.assertEqual(self.__7.preorderBreadthFirst(),
                         ['Khushi', 'Ariel', 'Tabitha', 'Ariana', 
                          'Jay', 'Luci', 'Zariyah'])
        self.assertEqual(self.__7.postorderBreadthFirst(),
                         ['Ariana', 'Jay', 'Luci', 'Zariyah',
                           'Ariel', 'Tabitha', 'Khushi'])

    def test15Structure(self) -> None:
        self.assertEqual(self.__15.preorder(), ['Khushi', 'Ariel', 'Ariana', 'Jay',
                                                'Caleb M.', 'Caleb D.', 'Elliott',
                                                'Tabitha', 'Luci', 'Nathan', 'Marco', 
                                                'Skyler', 'Zariyah', 'Trig', 'Tyson'])
        self.assertEqual(self.__15.postorder(), ['Ariana', 'Caleb D.', 'Elliott', 'Caleb M.',
                                                 'Jay', 'Ariel', 'Marco', 'Skyler', 'Nathan',
                                                 'Luci', 'Tyson', 'Trig', 'Zariyah', 
                                                 'Tabitha', 'Khushi'])
        self.assertEqual(self.__15.inorder(), ['Ariana', 'Ariel', 'Caleb D.', 'Caleb M.',
                                               'Elliott', 'Jay', 'Khushi', 'Luci',
                                               'Marco', 'Nathan', 'Skyler', 'Tabitha',
                                               'Trig', 'Tyson', 'Zariyah'])

    def testLen(self) -> None:
        self.assertEqual(len(self.__empty), 0)
        self.assertEqual(len(self.__1), 1)
        self.assertEqual(len(self.__4), 4)
        self.assertEqual(len(self.__7), 7)
        self.assertEqual(len(self.__15), 15)

    def testGetNode(self) -> None:
        for s in (self._present_values + self._absent_values):
            with self.subTest(s=s):
                with self.assertRaises(ValueError):
                    self.__empty.getNode(s)

        self.assertEqual(self.__1.getNode('Tabitha').data(), 'Tabitha')
        for s in self._absent_values:
            with self.subTest(s=s):
                with self.assertRaises(ValueError):
                    self.__1.getNode(s)
        
        for s in self.__4.inorder():
            with self.subTest(s=s):
                self.assertEqual(self.__4.getNode(s).data(), s)
        for s in self._absent_values:
            with self.subTest(s=s):
                with self.assertRaises(ValueError):
                    self.__4.getNode(s)

        for s in self._present_values[:7]:
            with self.subTest(s=s):
                self.assertEqual(self.__7.getNode(s).data(), s)
        for s in self._absent_values:
            with self.subTest(s=s):
                with self.assertRaises(ValueError):
                    self.__7.getNode(s)

        for s in self._present_values:
            with self.subTest(s=s):
                self.assertEqual(self.__15.getNode(s).data(), s)
        for s in self._absent_values:
            with self.subTest(s=s):
                with self.assertRaises(ValueError):
                    self.__15.getNode(s)



    def testContains(self) -> None:
        for s in (self._present_values + self._absent_values):
            with self.subTest(s=s):
                self.assertFalse(s in self.__empty)

        self.assertTrue('Tabitha' in self.__1)
        for s in self._absent_values:
            with self.subTest(s=s):
                self.assertFalse(s in self.__1)

        for s in self.__4.inorder():
            with self.subTest(s=s):
                self.assertTrue(s in self.__4)
        for s in self._absent_values:
            with self.subTest(s=s):
                self.assertFalse(s in self.__4)

        for s in self._present_values[:7]:
            with self.subTest(s=s):
                self.assertTrue(s in self.__7)
        for s in self._present_values[7:]:
            with self.subTest(s=s):
                self.assertFalse(s in self.__7)

        for s in self._absent_values:
            with self.subTest(s=s):
                self.assertFalse(s in self.__15)
        for s in self._present_values:
            with self.subTest(s=s):
                self.assertTrue(s in self.__15)
            
    def testRemoveFromEmpty(self) -> None:
        with self.assertRaises(ValueError):
            self.__empty.remove('Jay')

    def testRemoveNotPresent(self) -> None:
        with self.assertRaises(ValueError):
            self.__1.remove('Jay')
        with self.assertRaises(ValueError):
            self.__4.remove('Jay')

    def testRemoveLeaf(self) -> None:
        self.assertTrue('Skyler' in self.__15)
        self.__15.remove('Skyler')
        self.assertFalse('Skyler' in self.__15)
        # Still a proper BST
        self.assertTrue(self.__15._invariant()) # type: ignore

    def testRemoveOneChildLeft(self) -> None:
        self.assertTrue('Jay' in self.__15)
        self.__15.remove('Jay')
        self.assertFalse('Jay' in self.__15)
        # Still a proper BST
        self.assertTrue(self.__15._invariant()) # type: ignore
        self.assertTrue('Caleb M.' in self.__15)
        self.assertTrue('Caleb D.' in self.__15)
        self.assertTrue('Elliott' in self.__15)

    def testRemoveOneChildRight(self) -> None:
        self.assertTrue('Luci' in self.__15)
        self.__15.remove('Luci')
        self.assertFalse('Luci' in self.__15)
        # Still a proper BST
        self.assertTrue(self.__15._invariant()) # type: ignore
        self.assertTrue('Nathan' in self.__15)
        self.assertTrue('Marco' in self.__15)
        self.assertTrue('Skyler' in self.__15)

    def testRemoveTwoChildren(self) -> None:
        self.assertTrue('Tabitha' in self.__15)
        self.__15.remove('Tabitha')
        self.assertFalse('Tabitha' in self.__15)
        # Still a proper BST
        self.assertTrue(self.__15._invariant()) # type: ignore
        self.assertTrue('Luci' in self.__15)
        self.assertTrue('Nathan' in self.__15)
        self.assertTrue('Marco' in self.__15)
        self.assertTrue('Skyler' in self.__15)
        self.assertTrue('Zariyah' in self.__15)
        self.assertTrue('Trig' in self.__15)
        self.assertTrue('Tyson' in self.__15)

    def testfindSuccessor(self) -> None:
        values = ['Khushi', 'Ariel', 'Caleb M.', 'Tabitha', 'Luci',
                  'Nathan', 'Trig']
        inorder = self.__15.inorder()
        for val in values:
            with self.subTest(val=val):
                idx = inorder.index(val)
                self.assertEqual(self.__15.getNode(val).findSuccessor(),
                                 inorder[idx+1])

    #     nodes = self.__15.inorder()
    #     for i in range(len(nodes)-1):
    #         self.assertTrue(self.__15)


if __name__ == '__main__':
    unittest.main()

