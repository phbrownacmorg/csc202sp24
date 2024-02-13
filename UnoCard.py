from AbstractCard import AbstractCard

class UnoCard(AbstractCard):
    """Class to represent an Uno card."""

    # Class variables
    # BOTTOM_RANK defaults to 0
    TOP_RANK: int = 14
    TOP_COLOR_RANK: int = 12
    COLOR_RANKS: tuple[int, ...] = tuple(range(TOP_COLOR_RANK+1))
    COLOR_SUITS: tuple[str, ...] = ('red', 'yellow', 'green', 'blue')
    WILD_RANKS: tuple[int, ...] = tuple(range(TOP_COLOR_RANK+1,
                                              TOP_RANK+1))
    WILD_SUIT: str = 'wild'
    RANKS: tuple[int, ...] = COLOR_RANKS + WILD_RANKS
    SUITS: tuple[str, ...] = COLOR_SUITS + (WILD_SUIT,)
    RANK_NAMES: tuple[str, ...] = tuple(map(str, range(10))) \
                                  + ('skip', 'reverse', 'draw 2') \
                                  + ('', 'draw 4')
    
    def _invariant(self) -> bool:
        """Class invariant."""
        valid_color = self._suit in self.COLOR_SUITS \
            and self._rank in self.COLOR_RANKS
        valid_wild = self._suit == self.WILD_SUIT \
            and self._rank in self.WILD_RANKS
        return (valid_color or valid_wild)
    
    def __init__(self, rank: int, suit: str):
        """Create an UnoCard of the given RANK and SUIT."""
        # Strengthen the precondition
        # Pre:
        assert (rank in self.COLOR_RANKS and suit in self.COLOR_SUITS) \
            or (rank in self.WILD_RANKS and suit == self.WILD_SUIT)
        # Call the superclass constructor, 
        #   because it *does* the right thing
        super().__init__(rank, suit)
        # Postcondition is already called by the superclass constructor  

    @classmethod
    def make_deck(cls) -> list[AbstractCard]:
        """Make an Uno deck."""
        # Precondition: none
        deck: list[AbstractCard] = []

        # Append the 0's
        for suit in cls.COLOR_SUITS:
            deck.append(cls(0, suit))

        # Do the rest of the color cards
        for rank in cls.COLOR_RANKS[1:]:
            for suit in cls.COLOR_SUITS:
                for i in range(2):
                    deck.append(cls(rank, suit))

        # Wild cards
        for rank in cls.WILD_RANKS:
            for i in range(4):
                deck.append(cls(rank, cls.WILD_SUIT))

        # Postcondition:
        assert len(deck) == 108
        return deck