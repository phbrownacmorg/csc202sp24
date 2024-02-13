import unittest
# import the code you want to test here
from UnoCard import UnoCard

class TestUnoCard(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testTrue(self) -> None:
        self.assertEqual(UnoCard.SUITS, 
                         ('red', 'yellow', 'green', 'blue', 'wild'))
        
    def testSuitRed(self) -> None:
        self.assertEqual(UnoCard(3, 'red').suit(), 'red')

    def testSuitYellow(self) -> None:
        self.assertEqual(UnoCard(11, 'yellow').suit(), 'yellow')

    def test_rank_3(self) -> None:
        self.assertEqual(UnoCard(3, 'red').rank(), 3)

    def test_rank_11(self) -> None:
        self.assertEqual(UnoCard(11, 'yellow').rank(), 11)

    def test_rank_name_3(self) -> None:
        self.assertEqual(UnoCard(3, 'red').rank_name(), '3')

    def test_rank_name_11(self) -> None:
        self.assertEqual(UnoCard(11, 'yellow').rank_name(), 'reverse')

    def test_named_constructor(self) -> None:
        self.assertEqual((UnoCard.makeCard('skip', 'green')).suit(),
                         'green')

    def testSuitWild(self) -> None:
        self.assertEqual(UnoCard(13, 'wild').suit(), 'wild')

    def test_rank_wild(self) -> None:
        self.assertEqual(UnoCard(13, 'wild').rank(), 13)

    def test_rank_draw4(self) -> None:
        self.assertEqual(UnoCard(14, 'wild').rank(), 14)

    def test_rank_name_wild(self) -> None:
        self.assertEqual(UnoCard(13, 'wild').rank_name(), '')

    def test_rank_name_draw4(self) -> None:
        self.assertEqual(UnoCard(14, 'wild').rank_name(), 'draw 4')

    def test_str_red3(self) -> None:
        self.assertEqual(str(UnoCard(3, 'red')), 'red 3')

    def test_str_blue12(self) -> None:
        self.assertEqual(str(UnoCard(12, 'blue')), 'blue draw 2')

    def test_str_wild(self) -> None:
        self.assertEqual(str(UnoCard(13, 'wild')), 'wild')

    def test_str_wild14(self) -> None:
        self.assertEqual(str(UnoCard(14, 'wild')), 'wild draw 4')


if __name__ == '__main__':
    unittest.main()

