import abc

class AbstractCard(abc.ABC):
    """Abstract base class to represent a playing card of a kind that is
    defined by a rank and a suit.  Examples include regular (French)
    playing cards, Uno cards, cards of the several European styles
    that have mostly gone out of use, Mamluk cards, tarot cards, and
    a good many lesser-known types.  Cards are immutable once created."""

    # Class attributes: override in subclasses!
    BOTTOM_RANK = 0 # default value
    TOP_RANK = 0
    SUITS: tuple[str, ...] = ()
    RANKS: tuple[int, ...] = ()
    RANK_NAMES: tuple[str, ...] = ()

    def _invariant(self) -> bool:
        """Class invariant."""
        # Pre: none
        valid = self._suit in self.SUITS
        valid = valid and self._rank in self.RANKS
        # Post: valid is True iff self is a valid PlayingCard
        return valid
    
    def __init__(self, rank: int, suit: str):
        """Construct a card of the given RANK and SUIT."""
        # Pre:
        assert self.BOTTOM_RANK <= rank <= self.TOP_RANK \
            and suit in self.SUITS
        self._rank = rank
        self._suit = suit
        # Post:
        assert self._invariant()

    # QUERY METHODS
    
    def rank(self) -> int:
        """Return the card's rank."""
        return self._rank

    def suit(self) -> str:
        """Return the card's suit."""
        return self._suit

    def rank_name(self) -> str:
        """Return the name (a string) of the card's rank."""
        return self.RANK_NAMES[self._rank]
    
    def __str__(self) -> str:
        """String representation of a card."""
        return (self.suit() + ' ' + self.rank_name()).strip()
    
    def __eq__(self, other: object) -> bool:
        equal = hasattr(other, 'rank_name') and hasattr(other, 'suit')
        equal = equal and self.rank_name() == other.rank_name() and \
                        self.suit() == other.suit()
        return equal

    @classmethod
    def makeCard(cls, rankName: str, suit: str) -> 'AbstractCard':
        """Make a card from the given RANKNAME (a string) and SUIT.
        This factory function--also called a named constructor--just
        figures out the proper arguments to pass to the constructor,
        calls the constructor, and returns the new object."""
        # Pre:
        assert \
            rankName.lower() in \
                cls.RANK_NAMES[cls.BOTTOM_RANK:] \
            and suit in cls.SUITS
        card: cls = cls(
                        cls.RANK_NAMES.index(rankName.lower()),
                        suit)
        # Post: returns a PlayingCard of the specified suit and rank.
        # assert card._invariant() # Already asserted in the constructor
        return card

    @classmethod
    @abc.abstractmethod
    def make_deck(cls) -> list['AbstractCard']:
        """Make a deck of this kind of card.  Abstract."""
        return []
