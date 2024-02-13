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

    def test_eq(self) -> None:
        for rank in UnoCard.COLOR_RANKS:
            for suit in UnoCard.COLOR_SUITS:
                with self.subTest(rank = rank, suit = suit):
                    this_card = UnoCard(rank, suit)
                    self.assertEqual(this_card,
                                    UnoCard(rank, suit))
                        
                    # Now, the cases where the cards are *not* equal
                    for rank2 in UnoCard.COLOR_RANKS:
                        for suit2 in UnoCard.COLOR_SUITS:
                            if rank != rank2 or suit != suit2:
                                with self.subTest(rank2=rank2, suit2=suit2):
                                    self.assertNotEqual(this_card, 
                                                        UnoCard(rank2, suit2))

                    # A color card is never equal to a wild card
                    for rank2 in UnoCard.WILD_RANKS:
                        suit2 = UnoCard.WILD_SUIT
                        with self.subTest(rank2 = rank2, suit2=suit2):
                            self.assertNotEqual(this_card, 
                                                UnoCard(rank2, suit2))
        
        # Now, the wild cards
        for rank in UnoCard.WILD_RANKS:
            suit = UnoCard.WILD_SUIT
            this_card = UnoCard(rank, suit)
            with self.subTest(rank=rank, suit=suit):
                # Cases where they are equal
                self.assertEqual(this_card, UnoCard(rank, suit))

                # Cases where they are *not* equal
                # Wild cards are never equal to color cards
                for rank2 in UnoCard.COLOR_RANKS:
                    for suit2 in UnoCard.COLOR_SUITS:
                        with self.subTest(rank2=rank2, suit2=suit2):
                            self.assertNotEqual(this_card, 
                                                UnoCard(rank2, suit2))

                # Now, the wild card with the opposite suit
                for rank2 in UnoCard.WILD_RANKS:
                    suit2 = UnoCard.WILD_SUIT
                    if rank2 != rank:
                        with self.subTest(rank2=rank2, suit2=suit2):
                            self.assertNotEqual(this_card, 
                                                UnoCard(rank2, suit2))

            
    def test_make_deck(self) -> None:
        deck = UnoCard.make_deck()
        self.assertEqual(len(deck), 108)

        # Zeroes
        for i in range(4):
            with self.subTest(i=i):
                self.assertEqual(deck[i].rank(), 0)
                self.assertEqual(deck[i].rank_name(), '0')
                self.assertEqual(deck[i].suit(), UnoCard.SUITS[i])

        # Color cards
        for i in range(4, 100):
            with self.subTest(i=i):
                rank = ((i-4) // 8) + 1
                self.assertEqual(deck[i].rank(), rank)
                self.assertEqual(deck[i].rank_name(), UnoCard.RANK_NAMES[rank])
                self.assertEqual(deck[i].suit(), UnoCard.SUITS[((i-4) // 2) % 4])

        # Wild cards
        for i in range(100, len(deck)):
            with self.subTest(i=i):
                rank = ((i-100) // 4) + 13
                self.assertEqual(deck[i].rank(), rank)
                self.assertEqual(deck[i].rank_name(), UnoCard.RANK_NAMES[rank])
                self.assertEqual(deck[i].suit(), UnoCard.WILD_SUIT)

if __name__ == '__main__':
    unittest.main()

