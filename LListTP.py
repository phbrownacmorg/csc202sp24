from typing import cast, Generic, TypeVar
from LList import LList

T = TypeVar('T')


class LListTP(Generic[T]):
    """Class to represent a linked list with a tail pointer."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid = (self.__tail).empty() and (self.__head)._invariant()
        if self.empty():
            valid = valid and self.__head is self.__tail
        else:
            valid = valid and self.__head is not self.__tail
        return valid

    def __init__(self):
        """Create an empty LListTP[T]."""
        self.__head: LList[T] = LList[T]() # type: ignore
        self.__tail: LList[T] = self.__head
        # Post:
        assert self._invariant()

    # QUERY METHODS
        
    def empty(self) -> bool:
        """Return True iff the list is empty."""
        return (self.__head).empty()
    
    def value(self) -> T:
        """Returns the value at the head of the list."""
        # Pre:
        assert self._invariant() and not self.empty()
        return self.__head.value()

    def __len__(self) -> int:
        # Pre:
        assert self._invariant()
        return len(self.__head)

    def __str__(self) -> str:
        # Pre:
        assert self._invariant()
        return str(self.__head)

    def index(self, val: T) -> int:
        # Pre:
        assert self._invariant()
        return self.__head.index(val)

    # MUTATOR METHODS

    def add(self, val: T) -> None:
        # Pre:
        assert self._invariant()
        self.__head.add(val)
        # Adjust the tail pointer if adding to an empty list
        if self.__tail is self.__head:
            self.__tail = self.__tail.next()
        # Post:
        assert self._invariant()

    def pop(self, idx: int = -1) -> T:
        # Pre:
        assert self._invariant()
        return self.__head.pop(idx)
