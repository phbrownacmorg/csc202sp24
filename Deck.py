import random
from AbstractCard import AbstractCard
from typing import Iterable

class Deck:
    """Class to represent a deck of cards."""

    # Invariant is really just that every card in the Deck is an
    # AbstractCard, which should be pretty well covered by the
    # type checker

    def __init__(self): # type: ignore
        """Create an empty deck."""
        self._cards: list[AbstractCard] = []

    # Query methods
    def __len__(self) -> int:
        """Size of the deck is the number of cards in the deck."""
        return len(self._cards)

    def __str__(self) -> str:
        """String representation of the deck."""
        result = 'Deck, listed bottom to top:\n'
        for card in self._cards:
            # Polymorphism!! Each kind of card looks up its
            # own __str__() method *at runtime* and 
            # Does the Right Thing (tm) for the kind of card it is.
            result += '        ' + str(card) + '\n'
        return result

    # Mutator methods
    def addCard(self, newCard: AbstractCard) -> None:
        """Add a single card to the top of the deck."""
        # Pre: none
        self._cards.append(newCard)
        # Post: len(self) has increased by 1, and...
        assert self._cards[-1] == newCard

    def addToBottom(self, newCard: AbstractCard) -> None:
        """Add a single card to the bottom of the deck."""
        # Pre: none
        self._cards.insert(0, newCard)
        # Post: len(self) has increased by 1, and...
        assert self._cards[0] == newCard

    def addToMiddle(self, newCard: AbstractCard, idx: int = -1) -> None:
        """Add a single card to the middle of the deck at index IDX.
        If IDX is not provided, a random location is chosen."""
        # Pre:
        assert -1 <= idx <= len(self)
        if idx < 0:
            idx = random.randrange(len(self) + 1)
        self._cards.insert(idx, newCard)
        # Post: len(self) has increased by 1, and...
        assert self._cards[idx] == newCard

    def add(self, others: Iterable[AbstractCard]) -> None:
        # Pre: none
        self._cards.extend(others)
        # Post: len(self) == old len(self) + len(other)
        #         and all the cards in other are in deck

    def deal(self) -> AbstractCard:
        # Pre:
        assert len(self._cards) > 0, "Can't deal from an empty deck"
        topCard: AbstractCard = self._cards.pop()
        # Post: len(self._cards) has decreased by 1, and
        #         return value is the old top card
        return topCard
    
    def shuffle(self) -> None:
        """Shuffle the deck."""
        # Set the number of iterations before starting
        size = len(self._cards)
        newcards: list[AbstractCard] = []
        for i in range(size):
            newcards.append(random.choice(self._cards))
        self._cards = newcards
