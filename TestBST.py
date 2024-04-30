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
        self.__15.add('Skyler')

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

    def testContains(self) -> None:
        present_values = self.__15.preorderBreadthFirst()
        absent_values = ['Alice', 'Arid', 'Brandon', 'Caleb E.', 'Daniel', 'Grayson',
                         'Kennedy', 'Laura', 'Lydia', 'Maggie', 'Olivia', 'Stirling',
                         'Tom', 'Tucker', 'Washington', 'Zelda']
        for s in (present_values + absent_values):
            with self.subTest(s=s):
                self.assertFalse(s in self.__empty)
        self.assertTrue('Tabitha' in self.__1)
        for s in absent_values:
            with self.subTest(s=s):
                self.assertFalse(s in self.__1)
        for s in self.__4.inorder():
            with self.subTest(s=s):
                self.assertTrue(s in self.__4)
        for s in absent_values:
            with self.subTest(s=s):
                self.assertFalse(s in self.__4)
        for s in present_values[:7]:
            with self.subTest(s=s):
                self.assertTrue(s in self.__7)
        for s in present_values[7:]:
            with self.subTest(s=s):
                self.assertFalse(s in self.__7)
        for s in absent_values:
            with self.subTest(s=s):
                self.assertFalse(s in self.__15)
        for s in present_values:
            with self.subTest(s=s):
                self.assertTrue(s in self.__15)
            



    # def testEmptyTrue(self) -> None:
    #     self.assertTrue(self.__empty.empty())

    # def testEmptyFalse(self) -> None:
    #     self.assertFalse(self.__1.empty())
    #     self.assertFalse(self.__4.empty())

    # def testData(self) -> None:
    #     with self.assertRaises(AssertionError):
    #         self.__empty.data()
    #     self.assertEqual(self.__1.data(), 'Tabitha')
    #     self.assertEqual(self.__4.data(), 'Ariel')
    #     self.assertEqual(self.__4.left().data(), 'Ariana')
    #     self.assertEqual(self.__4.right().data(), 'Luci')
    #     self.assertEqual(self.__4.right().left().data(), 'Elliott')

    # def testLen(self) -> None:
    #     self.assertEqual(len(self.__empty), 0)
    #     self.assertEqual(len(self.__1), 1)
    #     self.assertEqual(len(self.__4), 4)

    # def testHeight(self) -> None:
    #     self.assertEqual(self.__empty.height(), 0)
    #     self.assertEqual(self.__1.height(), 1)
    #     self.assertEqual(self.__4.height(), 3)

    # def testPreorder(self) -> None:
    #     self.assertEqual(self.__empty.preorder(), [])
    #     self.assertEqual(self.__1.preorder(), ['Tabitha'])
    #     self.assertEqual(self.__4.preorder(), ['Ariel', 'Ariana', 'Luci', 'Elliott'])
    #     self.assertEqual(self.__7.preorder(), ['Jay', 'Ariel', 'Ariana', 'Khushi',
    #                                            'Tabitha', 'Luci', 'Zariyah'])

    # def testPostorder(self) -> None:
    #     self.assertEqual(self.__empty.postorder(), [])
    #     self.assertEqual(self.__1.postorder(), ['Tabitha'])
    #     self.assertEqual(self.__4.postorder(), ['Ariana', 'Elliott', 'Luci', 'Ariel'])
    #     self.assertEqual(self.__7.postorder(), ['Ariana', 'Khushi', 'Ariel', 'Luci',
    #                                             'Zariyah', 'Tabitha', 'Jay'])

    # def testInorder(self) -> None:
    #     self.assertEqual(self.__empty.inorder(), [])
    #     self.assertEqual(self.__1.inorder(), ['Tabitha'])
    #     self.assertEqual(self.__4.inorder(), ['Ariana', 'Ariel', 'Elliott', 'Luci'])
    #     self.assertEqual(self.__7.inorder(), ['Ariana', 'Ariel', 'Khushi', 'Jay',
    #                                           'Luci', 'Tabitha', 'Zariyah'])

    # def testPreorderBreadthFirst(self) -> None:
    #     self.assertEqual(self.__empty.preorderBreadthFirst(), [])
    #     self.assertEqual(self.__1.preorderBreadthFirst(), ['Tabitha'])
    #     self.assertEqual(self.__4.preorderBreadthFirst(), 
    #                      ['Ariel', 'Ariana', 'Luci', 'Elliott'])
    #     self.assertEqual(self.__7.preorderBreadthFirst(),
    #                      ['Jay', 'Ariel', 'Tabitha', 'Ariana', 'Khushi', 'Luci', 'Zariyah'])

    # def testPostorderBreadthFirst(self) -> None:
    #     self.assertEqual(self.__empty.postorderBreadthFirst(), [])
    #     self.assertEqual(self.__1.postorderBreadthFirst(), ['Tabitha'])
    #     self.assertEqual(self.__4.postorderBreadthFirst(), 
    #                      ['Elliott', 'Ariana', 'Luci', 'Ariel'])
    #     self.assertEqual(self.__7.postorderBreadthFirst(),
    #                      ['Ariana', 'Khushi', 'Luci', 'Zariyah', 'Ariel', 'Tabitha', 'Jay'])
    #     self.assertEqual(self.__15.postorderBreadthFirst(),
    #                      ['Nathan', 'Caleb D.', 'Caleb M.', 'Marco', 
    #                       'Elliott', 'Skyler', 'Trig', 'Tyson',
    #                       'Ariana', 'Khushi', 'Luci', 'Zariyah', 
    #                       'Ariel', 'Tabitha', 'Jay'])


if __name__ == '__main__':
    unittest.main()

