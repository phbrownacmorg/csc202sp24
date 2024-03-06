from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    """Class to represent a stack of T.  The stack is implemented as a
    list, with the end of the list being the top of the stack."""

    def __init__(self): # type: ignore
        """Create an empty stack."""
        self.__items: list[T] = []

    # Query methods
    def empty(self) -> bool:
        """Return True iff the stack is empty."""
        return len(self.__items) == 0
    
    def peek(self) -> T:
        """Peek at the top item on the stack."""
        # Pre:
        assert len(self.__items) > 0
        return self.__items[-1]
    
    # Mutator methods
    def push(self, new_item: T) -> None:
        """Add NEW_ITEM to the top of the stack."""
        self.__items.append(new_item)

    def pop(self) -> T:
        """Remove and return the top item from the stack.  The stack
        musty not be empty."""
        # Pre:
        assert len(self.__items) > 0
        return self.__items.pop()
