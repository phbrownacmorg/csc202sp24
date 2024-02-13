from AbstractCard import AbstractCard

class PlayingCard(AbstractCard):
    """Class to represent a playing card of the (historically)
    French style; that is, the suits are hearts, diamonds, 
    clubs, and spades, and the ranks are ace through 10, jack,
    queen, and king."""

    # Class attributes
    TOP_RANK = 13
    BOTTOM_RANK = 1
    SUITS: tuple[str, ...] = ('clubs', 'diamonds', 'hearts', 'spades')
    RANKS: tuple[int, ...] = tuple(range(BOTTOM_RANK, TOP_RANK+1))
    RANK_NAMES: tuple[str, ...] = ('', 'ace') + tuple(map(str, range(2,11))) \
                                + ('jack', 'queen', 'king')

    @classmethod
    def make_deck(cls) -> list[AbstractCard]:
        """Make a deck of regular playing cards."""
        deck : list[AbstractCard] = []
        for rank in range(PlayingCard.BOTTOM_RANK, PlayingCard.TOP_RANK+1):
            for suit in PlayingCard.SUITS:
                deck.append(PlayingCard(rank, suit))

        # Post
        assert len(deck) == 52
        return deck