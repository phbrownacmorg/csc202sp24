class PlayingCard:
    """Class to represent a playing card of the (historically)
    French style; that is, the suits are hearts, diamonds, 
    clubs, and spades, and the ranks are ace through 10, jack,
    queen, and king.  Cards are immutable once created."""

    # Class attributes
    TOP_RANK = 13
    BOTTOM_RANK = 1
    SUITS: tuple[str, ...] = ('clubs', 'diamonds', 'hearts', 'spades')
    RANKS: tuple[int, ...] = tuple(range(BOTTOM_RANK, TOP_RANK+1))
    RANK_NAMES: tuple[str, ...] = ('', 'ace') + tuple(map(str, range(2,11))) \
                                + ('jack', 'queen', 'king')
    
    def _invariant(self) -> bool:
        # Pre: none
        valid = self._suit in self.SUITS
        valid = valid and self.BOTTOM_RANK <= self._rank <= self.TOP_RANK
        # Post: valid is True iff self is a valid PlayingCard
        return valid

    def __init__(self, rank: int, suit: str):
        # Pre:
        assert self.BOTTOM_RANK <= rank <= self.TOP_RANK \
            and suit in self.SUITS
        self._rank = rank
        self._suit = suit
        # Post:
        assert self._invariant()

    # QUERY METHODS
    
    def rank(self) -> int:
        return self._rank

    def suit(self) -> str:
        return self._suit

    def rank_name(self) -> str:
        return self.RANK_NAMES[self._rank]

    # "Named constructor".  Also called a "factory function".
    @classmethod
    def makeCard(cls, rankName: str, suit: str) -> 'PlayingCard':
        # Pre:
        assert \
            rankName.lower() in \
                PlayingCard.RANK_NAMES[PlayingCard.BOTTOM_RANK:] \
            and suit in PlayingCard.SUITS
        card: PlayingCard = PlayingCard(
                        PlayingCard.RANK_NAMES.index(rankName.lower()),
                        suit)
        # Post: returns a PlayingCard of the specified suit and rank.
        # assert card._invariant() # Already asserted in the constructor
        return card

    @classmethod
    def make_deck(cls) -> list['PlayingCard']:
        deck : list[PlayingCard] = []
        for rank in range(PlayingCard.BOTTOM_RANK, PlayingCard.TOP_RANK+1):
            for suit in PlayingCard.SUITS:
                deck.append(PlayingCard(rank, suit))

        # Post
        assert len(deck) == 52
        return deck