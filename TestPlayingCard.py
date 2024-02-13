import unittest
# import the code you want to test here

from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testTrue(self) -> None:
        self.assertEqual(PlayingCard.TOP_RANK, 13)

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
        
    def test_str_jack_hearts(self) -> None:
        self.assertEqual(str(PlayingCard(11, 'hearts')), 'jack of hearts')

    def test_str_king_clubs(self) -> None:
        self.assertEqual(str(PlayingCard(13, 'clubs')), 'king of clubs')

    def test_str_ace_spades(self) -> None:
        self.assertEqual(str(PlayingCard(1, 'spades')), 'ace of spades')

    def test_str_3_clubs(self) -> None:
        self.assertEqual(str(PlayingCard(3, 'clubs')), '3 of clubs')

    def test_str_10_diamonds(self) -> None:
        self.assertEqual(str(PlayingCard(10, 'diamonds')), '10 of diamonds')

    def test_eq(self) -> None:
        for rank in PlayingCard.RANKS:
            with self.subTest(rank = rank):
                for suit in PlayingCard.SUITS:
                    with self.subTest(suit = suit):
                        this_card = PlayingCard(rank, suit)
                        self.assertEqual(this_card,
                                        PlayingCard(rank, suit))
                        
                        # Now, the cases where the cards are *not* equal
                        for rank2 in PlayingCard.RANKS:
                            for suit2 in PlayingCard.SUITS:
                                if rank != rank2 or suit != suit2:
                                    with self.subTest(rank2 = rank2, suit2=suit2):
                                        self.assertNotEqual(this_card, PlayingCard(rank2, suit2))
            
    def test_make_deck(self) -> None:
        deck = PlayingCard.make_deck()
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

