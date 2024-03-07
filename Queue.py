from typing import Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """Class to represent a queue, based on a Python list.
    The head of the queue is at index 0, and the tail is
    at the end of the list."""

    def __init__(self):
        """Construct an empty queue."""
        self.__items: list[T] = []

    # Query methods
    def empty(self) -> bool:
        """Return True iff the queue is empty."""
        return len(self.__items) == 0

    def peek(self) -> T:
        """Peek at the item at the head of the queue."""
        # Pre:
        assert len(self.__items) > 0
        return self.__items[0]

    # Mutator methods
    def add(self, new_item: T) -> None:
        """Add NEW_ITEM to the end of the queue."""
        self.__items.append(new_item)

    def pop(self) -> T:
        """Remove and return the item at the head of the queue.
        The queue must not be empty."""
        # Pre:
        assert len(self.__items) > 0
        return self.__items.pop(0)
