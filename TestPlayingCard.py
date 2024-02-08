import unittest
# import the code you want to test here

from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testTrue(self) -> None:
        self.assertEqual(PlayingCard(3, 'clubs').TOP_RANK, 13)

    def testSuitClubs(self) -> None:
        self.assertEqual(PlayingCard(3, 'clubs').suit(), 'clubs')

    def testSuitDiamonds(self) -> None:
        self.assertEqual(PlayingCard(11, 'diamonds').suit(), 'diamonds')

    def test_rank_3(self) -> None:
        self.assertEqual(PlayingCard(3, 'clubs').rank(), 3)

    def test_rank_11(self) -> None:
        self.assertEqual(PlayingCard(11, 'diamonds').rank(), 11)

    def test_rank_name_3(self) -> None:
        self.assertEqual(PlayingCard(3, 'clubs').rank_name(), '3')

    def test_rank_name_11(self) -> None:
        self.assertEqual(PlayingCard(11, 'diamonds').rank_name(), 'jack')

    def test_named_constructor(self) -> None:
        self.assertEqual((PlayingCard.makeCard('Jack', 'hearts')).suit(),
                         'hearts')
        
    def test_make_deck(self) -> None:
        deck: list[PlayingCard] = PlayingCard.make_deck()
        self.assertEqual(len(deck), 52)
        for i in range(52):
            with self.subTest(i=i):
                self.assertEqual(deck[i].rank(), 
                                 (i // len(PlayingCard.SUITS)+1))
                self.assertEqual(deck[i].suit(),
                                 PlayingCard.SUITS[i % len(PlayingCard.SUITS)])
                self.assertEqual(deck[i].rank_name(),
                                 PlayingCard.RANK_NAMES[i // len(PlayingCard.SUITS) + 1])

if __name__ == '__main__':
    unittest.main()

