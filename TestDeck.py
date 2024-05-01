import random
import unittest
# import the code you want to test here
from Deck import Deck
from PlayingCard import PlayingCard
from UnoCard import UnoCard

class TestDeck(unittest.TestCase):

    # setUp() will be run before each test method
    def setUp(self) -> None:
        # Empty deck
        self._empty = Deck() # type: ignore

        # 52-card deck of PlayingCard
        self._52 = Deck() # type: ignore
        self._52.add(PlayingCard.make_deck())

        # 108-card Uno deck
        self._108 = Deck() # type: ignore
        self._108.add(UnoCard.make_deck())

        self._160 = Deck() # type: ignore
        self._160.add(PlayingCard.make_deck())
        self._160.add(UnoCard.make_deck())

        # Here because random is used both by testShuffle() and
        # testAddToMiddle...  Don't Repeat Yourself.
        random.seed(401)


    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testLenEmpty(self) -> None:
        self.assertEqual(len(Deck()), 0) # type: ignore

    def testLen52(self) -> None:
        self.assertEqual(len(self._52), 52)

    def testLen108(self) -> None:
        self.assertEqual(len(self._108), 108)

    def testLen160(self) -> None:
        self.assertEqual(len(self._160), 160)

    def testDeal52(self) -> None:
        top_card = self._52.deal()
        self.assertEqual(len(self._52), 51)
        self.assertEqual(top_card, PlayingCard.makeCard('King', 'spades'))

    def testDeal108(self) -> None:
        top_card = self._108.deal()
        self.assertEqual(len(self._108), 107)
        self.assertEqual(top_card, UnoCard.makeCard('draw 4', 'wild'))

    def testDeal160(self) -> None:
        top_card = self._160.deal()
        self.assertEqual(len(self._160), 159)
        self.assertEqual(top_card, UnoCard.makeCard('draw 4', 'wild'))

    def testAdd1ToEmpty(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._empty.addCard(new_card)
        self.assertEqual(len(self._empty), 1)
        self.assertEqual(self._empty.deal(), new_card)

    def testAdd1To52(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._52.addCard(new_card)
        self.assertEqual(len(self._52), 53)
        self.assertEqual(self._52.deal(), new_card)

    def testAdd1To108(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._108.addCard(new_card)
        self.assertEqual(len(self._108), 109)
        self.assertEqual(self._108.deal(), new_card)

    def testAddBottomToEmpty(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._empty.addToBottom(new_card)
        self.assertEqual(len(self._empty), 1)
        self.assertEqual(self._empty.deal(), new_card)

    def testAddBottomTo52(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._52.addToBottom(new_card)
        self.assertEqual(len(self._52), 53)
        for i in range(52): # Get rid of the top 52 cards
            self._52.deal()
        self.assertEqual(self._52.deal(), new_card)

    def testAddMiddleToEmpty(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._empty.addToMiddle(new_card)
        self.assertEqual(len(self._empty), 1)
        self.assertEqual(self._empty.deal(), new_card)

    def testAddMiddleTo52(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._52.addToMiddle(new_card) # Random location, 31 with this seed
        self.assertEqual(len(self._52), 53)
        #print(self._52)
        for i in range(52-31): # Get rid of the top 21 cards
            self._52.deal()
        self.assertEqual(self._52.deal(), new_card)

    def testAddMiddle0To52(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._52.addToMiddle(new_card, 0)
        self.assertEqual(len(self._52), 53)
        for i in range(52): # Get rid of the top 52 cards
            self._52.deal()
        self.assertEqual(self._52.deal(), new_card)

    def testAddMiddle52To52(self) -> None:
        new_card = PlayingCard.makeCard('Queen', 'Hearts')
        self._52.addToMiddle(new_card, 52)
        self.assertEqual(len(self._52), 53)
        self.assertEqual(self._52.deal(), new_card)


    def testStrEmpty(self) -> None:
        self.assertEqual(str(self._empty), 'Deck, listed bottom to top:\n')

    def testStr52(self) -> None:
        #print(self._52)
        self.assertEqual(str(self._52), """Deck, listed bottom to top:
        ace of clubs
        ace of diamonds
        ace of hearts
        ace of spades
        2 of clubs
        2 of diamonds
        2 of hearts
        2 of spades
        3 of clubs
        3 of diamonds
        3 of hearts
        3 of spades
        4 of clubs
        4 of diamonds
        4 of hearts
        4 of spades
        5 of clubs
        5 of diamonds
        5 of hearts
        5 of spades
        6 of clubs
        6 of diamonds
        6 of hearts
        6 of spades
        7 of clubs
        7 of diamonds
        7 of hearts
        7 of spades
        8 of clubs
        8 of diamonds
        8 of hearts
        8 of spades
        9 of clubs
        9 of diamonds
        9 of hearts
        9 of spades
        10 of clubs
        10 of diamonds
        10 of hearts
        10 of spades
        jack of clubs
        jack of diamonds
        jack of hearts
        jack of spades
        queen of clubs
        queen of diamonds
        queen of hearts
        queen of spades
        king of clubs
        king of diamonds
        king of hearts
        king of spades
""")

    def testStr108(self) -> None:
        #print(self._108)
        self.assertEqual(str(self._108), """Deck, listed bottom to top:
        blue 0
        green 0
        red 0
        yellow 0
        blue 1
        blue 1
        green 1
        green 1
        red 1
        red 1
        yellow 1
        yellow 1
        blue 2
        blue 2
        green 2
        green 2
        red 2
        red 2
        yellow 2
        yellow 2
        blue 3
        blue 3
        green 3
        green 3
        red 3
        red 3
        yellow 3
        yellow 3
        blue 4
        blue 4
        green 4
        green 4
        red 4
        red 4
        yellow 4
        yellow 4
        blue 5
        blue 5
        green 5
        green 5
        red 5
        red 5
        yellow 5
        yellow 5
        blue 6
        blue 6
        green 6
        green 6
        red 6
        red 6
        yellow 6
        yellow 6
        blue 7
        blue 7
        green 7
        green 7
        red 7
        red 7
        yellow 7
        yellow 7
        blue 8
        blue 8
        green 8
        green 8
        red 8
        red 8
        yellow 8
        yellow 8
        blue 9
        blue 9
        green 9
        green 9
        red 9
        red 9
        yellow 9
        yellow 9
        blue skip
        blue skip
        green skip
        green skip
        red skip
        red skip
        yellow skip
        yellow skip
        blue reverse
        blue reverse
        green reverse
        green reverse
        red reverse
        red reverse
        yellow reverse
        yellow reverse
        blue draw 2
        blue draw 2
        green draw 2
        green draw 2
        red draw 2
        red draw 2
        yellow draw 2
        yellow draw 2
        wild
        wild
        wild
        wild
        wild draw 4
        wild draw 4
        wild draw 4
        wild draw 4
""")

    def testStr160(self) -> None:
        # print(self._160) # Polymorphic!  Each card knows how to print
        self.assertEqual(str(self._160), """Deck, listed bottom to top:
        ace of clubs
        ace of diamonds
        ace of hearts
        ace of spades
        2 of clubs
        2 of diamonds
        2 of hearts
        2 of spades
        3 of clubs
        3 of diamonds
        3 of hearts
        3 of spades
        4 of clubs
        4 of diamonds
        4 of hearts
        4 of spades
        5 of clubs
        5 of diamonds
        5 of hearts
        5 of spades
        6 of clubs
        6 of diamonds
        6 of hearts
        6 of spades
        7 of clubs
        7 of diamonds
        7 of hearts
        7 of spades
        8 of clubs
        8 of diamonds
        8 of hearts
        8 of spades
        9 of clubs
        9 of diamonds
        9 of hearts
        9 of spades
        10 of clubs
        10 of diamonds
        10 of hearts
        10 of spades
        jack of clubs
        jack of diamonds
        jack of hearts
        jack of spades
        queen of clubs
        queen of diamonds
        queen of hearts
        queen of spades
        king of clubs
        king of diamonds
        king of hearts
        king of spades
        blue 0
        green 0
        red 0
        yellow 0
        blue 1
        blue 1
        green 1
        green 1
        red 1
        red 1
        yellow 1
        yellow 1
        blue 2
        blue 2
        green 2
        green 2
        red 2
        red 2
        yellow 2
        yellow 2
        blue 3
        blue 3
        green 3
        green 3
        red 3
        red 3
        yellow 3
        yellow 3
        blue 4
        blue 4
        green 4
        green 4
        red 4
        red 4
        yellow 4
        yellow 4
        blue 5
        blue 5
        green 5
        green 5
        red 5
        red 5
        yellow 5
        yellow 5
        blue 6
        blue 6
        green 6
        green 6
        red 6
        red 6
        yellow 6
        yellow 6
        blue 7
        blue 7
        green 7
        green 7
        red 7
        red 7
        yellow 7
        yellow 7
        blue 8
        blue 8
        green 8
        green 8
        red 8
        red 8
        yellow 8
        yellow 8
        blue 9
        blue 9
        green 9
        green 9
        red 9
        red 9
        yellow 9
        yellow 9
        blue skip
        blue skip
        green skip
        green skip
        red skip
        red skip
        yellow skip
        yellow skip
        blue reverse
        blue reverse
        green reverse
        green reverse
        red reverse
        red reverse
        yellow reverse
        yellow reverse
        blue draw 2
        blue draw 2
        green draw 2
        green draw 2
        red draw 2
        red draw 2
        yellow draw 2
        yellow draw 2
        wild
        wild
        wild
        wild
        wild draw 4
        wild draw 4
        wild draw 4
        wild draw 4
""")
        
    def testShuffle(self) -> None:
        # Make the results pblueictable.
        self._52.shuffle()
        for i in range(52):
            with self.subTest(i=i):
                card = self._52.deal()
                cardvalue = 51 - ((card.rank() - 1) * len(card.SUITS) 
                                  + card.SUITS.index(card.suit()))
                self.assertNotEqual(i - cardvalue, 0)

if __name__ == '__main__':
    unittest.main()

